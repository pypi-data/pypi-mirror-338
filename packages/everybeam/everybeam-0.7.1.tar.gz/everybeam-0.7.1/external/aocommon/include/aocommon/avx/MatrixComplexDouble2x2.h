// Copyright (C) 2022 ASTRON (Netherlands Institute for Radio Astronomy)
// SPDX-License-Identifier: GPL-3.0-or-later

#ifndef AOCOMMON_AVX256_MATRIX_COMPLEX_DOUBLE_2X2_H
#define AOCOMMON_AVX256_MATRIX_COMPLEX_DOUBLE_2X2_H

#include "AvxMacros.h"
#include "DiagonalMatrixComplexDouble2x2.h"
#include "MatrixComplexFloat2x2.h"
#include "VectorComplexDouble2.h"

#include <aocommon/scalar/eigenvalues.h>
#include <aocommon/scalar/vector4.h>

#include <array>
#include <cassert>
#include <complex>
#include <immintrin.h>
#include <limits>
#include <ostream>

namespace aocommon::avx {

/**
 * Implements a 2x2 Matrix with complex double values.
 * The matrix is not initialized by default for performance considerations,
 * a call to Zero() can be used to do that when needed.
 *
 * This class is based on @ref aocommon::MC2x2 but uses AVX-256 instructions.
 */
class MatrixComplexDouble2x2 {
 public:
  AVX_TARGET MatrixComplexDouble2x2() noexcept = default;

  AVX_TARGET /* implicit */
  MatrixComplexDouble2x2(std::array<VectorComplexDouble2, 2> data) noexcept
      : data_{data} {}

  AVX_TARGET MatrixComplexDouble2x2(std::complex<double> a,
                                    std::complex<double> b,
                                    std::complex<double> c,
                                    std::complex<double> d) noexcept
      : data_{{VectorComplexDouble2{a, b}, VectorComplexDouble2{c, d}}} {}

  AVX_TARGET explicit MatrixComplexDouble2x2(
      DiagonalMatrixComplexDouble2x2 m) noexcept
      : MatrixComplexDouble2x2(m.Get(0), 0.0, 0.0, m.Get(1)) {}

  AVX_TARGET explicit MatrixComplexDouble2x2(
      const std::complex<float> matrix[4]) noexcept
      : data_{VectorComplexDouble2(&matrix[0]),
              VectorComplexDouble2(&matrix[2])} {}

  AVX_TARGET explicit MatrixComplexDouble2x2(
      MatrixComplexFloat2x2 matrix) noexcept {
    __m256 tmp = static_cast<__m256>(matrix);

    __m128 lo = _mm256_castps256_ps128(tmp);
    __m128 hi = _mm256_extractf128_ps(tmp, 1);
    data_[0] = VectorDouble4{_mm256_cvtps_pd(lo)};
    data_[1] = VectorDouble4{_mm256_cvtps_pd(hi)};
  }

  AVX_TARGET explicit MatrixComplexDouble2x2(
      const std::complex<double> matrix[4]) noexcept
      : data_{VectorComplexDouble2(&matrix[0]),
              VectorComplexDouble2(&matrix[2])} {}

  template <typename T>
  AVX_TARGET explicit MatrixComplexDouble2x2(const T* matrix) noexcept
      : data_{VectorComplexDouble2(matrix[0], matrix[1]),
              VectorComplexDouble2(matrix[2], matrix[3])} {}

  AVX_TARGET std::complex<double> Get(size_t index) const noexcept {
    assert(index < 4 && "Index out of bounds.");
    size_t array = index / 2;
    index %= 2;
    return data_[array].Get(index);
  }

  AVX_TARGET void Set(size_t index, std::complex<double> value) noexcept {
    assert(index < 4 && "Index out of bounds.");
    size_t array = index / 2;
    index %= 2;
    data_[array].Set(index, value);
  }

  AVX_TARGET MatrixComplexDouble2x2 Conjugate() const noexcept {
    return std::array<VectorComplexDouble2, 2>{data_[0].Conjugate(),
                                               data_[1].Conjugate()};
  }

  AVX_TARGET MatrixComplexDouble2x2 Transpose() const noexcept {
    // Note the compiler uses intrinsics without assistance.
    return MatrixComplexDouble2x2{Get(0), Get(2), Get(1), Get(3)};
  }

  /** @returns A^H * A. */
  AVX_TARGET MatrixComplexDouble2x2 HermitianSquare() const noexcept {
    // An explicit AVX version could be more efficient, but the use of this
    // method is rare so we have used a simpler implementation so far.
    return HermTranspose() * (*this);
  }

  AVX_TARGET bool Invert() noexcept {
    VectorComplexDouble2 v = data_[0] * VectorComplexDouble2{Get(3), Get(2)};

    std::complex<double> d = v.Get(0) - v.Get(1);
    if (d == std::complex<double>{}) return false;

    double n = std::norm(d);
    d.imag(-d.imag());
    __m256d reciprocal = _mm256_setr_pd(d.real(), d.imag(), d.real(), d.imag());

    v = VectorComplexDouble2{_mm256_div_pd(reciprocal, _mm256_set1_pd(n))};

    __m256d lo =
        _mm256_permute2f128_pd(static_cast<__m256d>(data_[0]),
                               static_cast<__m256d>(data_[1]), 0b0001'0011);
    __m256d hi =
        _mm256_permute2f128_pd(static_cast<__m256d>(data_[0]),
                               static_cast<__m256d>(data_[1]), 0b0000'0010);
    // XOR with +0.0 leaves the number unchanged.
    // XOR with -0.0 changes the sign of the value.
    lo = _mm256_xor_pd(lo, _mm256_setr_pd(0.0, 0.0, -0.0, -0.0));
    hi = _mm256_xor_pd(hi, _mm256_setr_pd(-0.0, -0.0, 0.0, 0.0));
    data_ = {VectorComplexDouble2{lo} * v, VectorComplexDouble2{hi} * v};
    return true;
  }

  /** Returns the sum of the diagonal elements. */
  AVX_TARGET std::complex<double> Trace() const noexcept {
    // Trace = M[0] + M[3]

    // Extract M[0] and M[1] as 128-bit AVX vector.
    __m128d ret = _mm256_castpd256_pd128(static_cast<__m256d>(data_[0]));
    // Extracts M[3] and M[4] as 128-bit AVX vector and adds it to ret.
    ret += _mm256_extractf128_pd(static_cast<__m256d>(data_[1]), 1);
    return {ret[0], ret[1]};
  }

  /** Assign data stored by 2x2 complex matrix to destination buffer */
  template <typename T>
  AVX_TARGET void AssignTo(T* destination) const noexcept {
    data_[0].AssignTo(destination);
    destination += 2;
    data_[1].AssignTo(destination);
  }

  AVX_TARGET static MatrixComplexDouble2x2 Zero() noexcept {
    return MatrixComplexDouble2x2{
        std::array{VectorComplexDouble2::Zero(), VectorComplexDouble2::Zero()}};
  }

  AVX_TARGET static MatrixComplexDouble2x2 Unity() noexcept {
    return MatrixComplexDouble2x2{
        std::complex<double>(1.0, 0.0), std::complex<double>(0.0, 0.0),
        std::complex<double>(0.0, 0.0), std::complex<double>(1.0, 0.0)};
  }

  AVX_TARGET static MatrixComplexDouble2x2 NaN() noexcept {
    return MatrixComplexDouble2x2{
        std::complex<double>{std::numeric_limits<double>::quiet_NaN(),
                             std::numeric_limits<double>::quiet_NaN()},
        std::complex<double>{std::numeric_limits<double>::quiet_NaN(),
                             std::numeric_limits<double>::quiet_NaN()},
        std::complex<double>{std::numeric_limits<double>::quiet_NaN(),
                             std::numeric_limits<double>::quiet_NaN()},
        std::complex<double>{std::numeric_limits<double>::quiet_NaN(),
                             std::numeric_limits<double>::quiet_NaN()}};
  }

  AVX_TARGET MatrixComplexDouble2x2& operator+=(
      MatrixComplexDouble2x2 value) noexcept {
    data_[0] += value.data_[0];
    data_[1] += value.data_[1];
    return *this;
  }

  AVX_TARGET MatrixComplexDouble2x2& operator-=(
      MatrixComplexDouble2x2 value) noexcept {
    data_[0] -= value.data_[0];
    data_[1] -= value.data_[1];
    return *this;
  }

  AVX_TARGET friend MatrixComplexDouble2x2 operator+(
      MatrixComplexDouble2x2 lhs, MatrixComplexDouble2x2 rhs) noexcept {
    return lhs += rhs;
  }

  AVX_TARGET friend MatrixComplexDouble2x2 operator-(
      MatrixComplexDouble2x2 lhs, MatrixComplexDouble2x2 rhs) noexcept {
    return lhs -= rhs;
  }

  AVX_TARGET friend MatrixComplexDouble2x2 operator*(
      MatrixComplexDouble2x2 lhs, MatrixComplexDouble2x2 rhs) noexcept {
    // The 2x2 matrix multiplication is done using the following algorithm.

    // High:
    // ret.a = lhs.a * rhs.a + lhs.b * rhs.c
    // ret.b = lhs.a * rhs.b + lhs.b * rhs.d
    //       | hc1   | hc2   | hc3   | hc4   |
    //       | hs1           | hs2           |

    // Low:
    // ret.c = lhs.c * rhs.a + lhs.d * rhs.c
    // ret.d = lhs.c * rhs.b + lhs.d * rhs.d
    //       | lc1   | lc2   | lc3   | lc4   |
    //       | ls1           | ls2           |

    // High:
    VectorComplexDouble2 hc1{lhs.Get(0), lhs.Get(0)};
    VectorComplexDouble2 hc2{rhs.Get(0), rhs.Get(1)};
    VectorComplexDouble2 hs1 = hc1 * hc2;

    VectorComplexDouble2 hc3{lhs.Get(1), lhs.Get(1)};
    VectorComplexDouble2 hc4{rhs.Get(2), rhs.Get(3)};
    VectorComplexDouble2 hs2 = hc3 * hc4;

    VectorComplexDouble2 hr = hs1 + hs2;

    // Low:
    VectorComplexDouble2 lc1{lhs.Get(2), lhs.Get(2)};
    VectorComplexDouble2 lc2{rhs.Get(0), rhs.Get(1)};
    VectorComplexDouble2 ls1 = lc1 * lc2;

    VectorComplexDouble2 lc3{lhs.Get(3), lhs.Get(3)};
    VectorComplexDouble2 lc4{rhs.Get(2), rhs.Get(3)};
    VectorComplexDouble2 ls2 = lc3 * lc4;

    VectorComplexDouble2 lr = ls1 + ls2;

    return std::array<VectorComplexDouble2, 2>{hr, lr};
  }

  /**
   * Matrix multiplication, alias for the overloaded * operator and thus equally
   * computationally efficient.
   */
  AVX_TARGET MatrixComplexDouble2x2
  Multiply(MatrixComplexDouble2x2 rhs) const noexcept {
    return *this * rhs;
  }

  /**
   * Matrix multiplication of internal matrix with Hermitian transpose of input
   * matrix, i.e. returns A * B^H. Note that this is preferred over combining
   * operator* with HermTranspose() for computational efficiency in the non-AVX
   * case.
   */
  AVX_TARGET MatrixComplexDouble2x2
  MultiplyHerm(MatrixComplexDouble2x2 rhs) const noexcept {
    return *this * rhs.HermTranspose();
  }

  /**
   * Matrix multiplication Hermitian transpose of internal matrix with input
   * matrix, i.e. returns A^H * B. Note that this is preferred over combining
   * operator* with HermTranspose() for computational efficiency in the non-AVX
   * case.
   */
  AVX_TARGET MatrixComplexDouble2x2
  HermThenMultiply(MatrixComplexDouble2x2 rhs) const noexcept {
    return HermTranspose() * rhs;
  }

  /**
   * Matrix multiplication of Hermitian transposes of both the internal matrix
   * and the input matrix, i.e. returns A^H * B^H. Note that this is preferred
   * over combining operator* with HermTranspose() for computational efficiency
   * in the non-AVX case.
   */
  AVX_TARGET MatrixComplexDouble2x2
  HermThenMultiplyHerm(MatrixComplexDouble2x2 rhs) const noexcept {
    return HermTranspose() * rhs.HermTranspose();
  }

  AVX_TARGET DiagonalMatrixComplexDouble2x2 Diagonal() const noexcept {
    return DiagonalMatrixComplexDouble2x2(data_[0].Get(0), data_[1].Get(1));
  }

  AVX_TARGET friend MatrixComplexDouble2x2 operator*(
      MatrixComplexDouble2x2 lhs, std::complex<double> rhs) noexcept {
    return std::array<VectorComplexDouble2, 2>{lhs.data_[0] * rhs,
                                               lhs.data_[1] * rhs};
  }

  AVX_TARGET friend MatrixComplexDouble2x2 operator*(
      std::complex<double> lhs, MatrixComplexDouble2x2 rhs) noexcept {
    return rhs * lhs;
  }

  AVX_TARGET friend MatrixComplexDouble2x2 operator*(
      MatrixComplexDouble2x2 lhs, DiagonalMatrixComplexDouble2x2 rhs) noexcept {
    // The multiplication of a 2x2 matrix M with a diagonal 2x2 matrix D is
    // not commutative and R = M * D can be written as
    // r[0][0] = m[0][0] * d[0][0] -> lhs[0] * rhs[0]
    // r[0][1] = m[0][1] * d[1][1] -> lhs[1] * rhs[1]
    // r[1][0] = m[1][0] * d[0][0] -> lhs[2] * rhs[0]
    // r[1][1] = m[1][1] * d[1][1] -> lhs[3] * rhs[1]
    return std::array<VectorComplexDouble2, 2>{lhs.data_[0] * rhs.Data(),
                                               lhs.data_[1] * rhs.Data()};
  }

  AVX_TARGET friend MatrixComplexDouble2x2 operator*(
      DiagonalMatrixComplexDouble2x2 lhs, MatrixComplexDouble2x2 rhs) noexcept {
    // The multiplication of a diagonal 2x2 matrix D with a 2x2 matrix M is
    // not commutative and R = D * M can be written as:
    // r[0][0] = d[0][0] * m[0][0] -> lhs[0] * rhs[0]
    // r[0][1] = d[0][0] * m[0][1] -> lhs[0] * rhs[1]
    // r[1][0] = d[1][1] * m[1][0] -> lhs[1] * rhs[2]
    // r[1][1] = d[1][1] * m[1][1] -> lhs[1] * rhs[3]
    return std::array<VectorComplexDouble2, 2>{
        lhs.Data().Get(0) * rhs.data_[0], lhs.Data().Get(1) * rhs.data_[1]};
  }

  AVX_TARGET MatrixComplexDouble2x2& operator*=(
      MatrixComplexDouble2x2 value) noexcept {
    *this = *this * value;
    return *this;
  }

  template <typename T>
  AVX_TARGET MatrixComplexDouble2x2& operator*=(const T* value) noexcept {
    *this = *this * MatrixComplexDouble2x2(value);
    return *this;
  }

  template <typename T>
  AVX_TARGET friend MatrixComplexDouble2x2 operator*(MatrixComplexDouble2x2 lhs,
                                                     const T* rhs) noexcept {
    return lhs * MatrixComplexDouble2x2(rhs);
  }

  AVX_TARGET friend bool operator==(MatrixComplexDouble2x2 lhs,
                                    MatrixComplexDouble2x2 rhs) noexcept {
    return lhs.data_ == rhs.data_;
  }

  AVX_TARGET friend std::ostream& operator<<(std::ostream& output,
                                             MatrixComplexDouble2x2 value) {
    output << "[{" << value.Get(0) << ", " << value.Get(1) << "}, {"
           << value.Get(2) << ", " << value.Get(3) << "}]";
    return output;
  }

  AVX_TARGET MatrixComplexDouble2x2 HermTranspose() const noexcept {
    return Transpose().Conjugate();
  }

  /**
   * Flatten 2x2 matrix to length 4 vector
   */
  AVX_TARGET Vector4 Vec() const {
    return Vector4(data_[0].Get(0), data_[1].Get(0), data_[0].Get(1),
                   data_[1].Get(1));
  }

  /**
   * Decompose a Hermitian matrix X into A A^H such that
   *   X = A A^H = U D D^H U^H
   *   with A = U D
   * where D D^H = E is a diagonal matrix
   *       with the eigen values of X, and U contains the eigen vectors.
   */
  AVX_TARGET MatrixComplexDouble2x2 DecomposeHermitianEigenvalue() const {
    std::complex<double> e1, e2, vec1[2], vec2[2];
    std::complex<double> values[4];
    AssignTo(values);
    EigenValuesAndVectors(values, e1, e2, vec1, vec2);
    double v1norm = std::norm(vec1[0]) + std::norm(vec1[1]);
    vec1[0] /= std::sqrt(v1norm);
    vec1[1] /= std::sqrt(v1norm);
    double v2norm = std::norm(vec2[0]) + std::norm(vec2[1]);
    vec2[0] /= std::sqrt(v2norm);
    vec2[1] /= std::sqrt(v2norm);

    return MatrixComplexDouble2x2(
        vec1[0] * std::sqrt(e1.real()), vec2[0] * std::sqrt(e2.real()),
        vec1[1] * std::sqrt(e1.real()), vec2[1] * std::sqrt(e2.real()));
  }

  AVX_TARGET std::complex<double> DoubleDot(MatrixComplexDouble2x2 rhs) const {
    return Get(0) * rhs.Get(0) + Get(1) * rhs.Get(1) + Get(2) * rhs.Get(2) +
           Get(3) * rhs.Get(3);
  }

  /// Element-wise product
  AVX_TARGET friend MatrixComplexDouble2x2 ElementProduct(
      MatrixComplexDouble2x2 lhs, MatrixComplexDouble2x2 rhs) {
    return MatrixComplexDouble2x2(
        std::array{lhs.data_[0] * rhs.data_[0], lhs.data_[1] * rhs.data_[1]});
  }

 private:
  std::array<VectorComplexDouble2, 2> data_;

  friend class MatrixComplexFloat2x2;
  AVX_TARGET friend double Norm(MatrixComplexDouble2x2 matrix) noexcept;
};

AVX_TARGET inline MatrixComplexDouble2x2 HermTranspose(
    MatrixComplexDouble2x2 matrix) noexcept {
  return matrix.HermTranspose();
}

/** Returns the sum of the diagonal elements. */
AVX_TARGET inline std::complex<double> Trace(
    MatrixComplexDouble2x2 matrix) noexcept {
  return matrix.Trace();
}

AVX_TARGET inline DiagonalMatrixComplexDouble2x2 Diagonal(
    MatrixComplexDouble2x2 matrix) noexcept {
  return matrix.Diagonal();
}

AVX_TARGET inline MatrixComplexFloat2x2::MatrixComplexFloat2x2(
    const MatrixComplexDouble2x2& matrix) noexcept {
  __m256 lo = _mm256_castps128_ps256(
      _mm256_cvtpd_ps(static_cast<__m256d>(matrix.data_[0])));
  __m128 hi = _mm256_cvtpd_ps(static_cast<__m256d>(matrix.data_[1]));

  *this = VectorComplexFloat4{_mm256_insertf128_ps(lo, hi, 1)};
}

AVX_TARGET inline double Norm(MatrixComplexDouble2x2 matrix) noexcept {
  // Norm Matrix Complex 2x2
  // Norm(a) + Norm(b) + Norm(c) + Norm(d)
  //
  // Norm is using C++'s definition of std::complex<T>::norm(). This norm is
  // also known as the 'field norm' or 'absolute square'. Norm is defined as
  // a.re * a.re + a.im * a.im
  //
  // Note if we want to do this according to the rules above some shuffling
  // needs to be done. Instead we can consider the underlying data an array
  // of 8 doubles. Then Norm becomes
  //
  // -- 7
  // \.
  //  .  a[n] * a[n]
  // /
  // -- n = 0
  //
  // and no shuffling in needed instead use the following algorithm
  //
  // hi = data_[0]
  // lo = data_[1]
  //
  // hi = hi * hi
  // lo = lo * lo
  //
  // tmp = hi + lo
  // ret = std::accumulate(&tmp[0], &tmp[4], 0.0); // not possible in C++
  //
  // instead of calculating tmp as described it can be done by
  // hi = lo * lo + hi

  __m256d hi = static_cast<__m256d>(matrix.data_[0]);
  __m256d lo = static_cast<__m256d>(matrix.data_[1]);

  hi *= hi;
  hi = _mm256_fmadd_pd(lo, lo, hi);

  // Summing the 4 elements in hi can be simply done by
  // return hi[0] + hi[1] + hi[2] + hi[3]
  //
  // however this is slow, it's more efficient to permutate the data and use
  // vector adding. The instruction set has a hadd operation, but this is
  // slow too. Instead use register permutations and additions. The entries
  // marked with - in the table mean we don't care about the contents. The
  // result will be stored in hi[0]:
  //
  // hi | a             | b     | c | d |
  // lo | c             | d     | - | - |
  //    --------------------------------- +
  // hi | a + c         | b + d | - | - |
  // lo | b + d         | -     | - | - |
  //    --------------------------------- +
  // hi | a + c + b + d | -     | - | - |

  lo = _mm256_permute4x64_pd(hi, 0b11'10);
  hi += lo;

  __m128d ret = _mm256_castpd256_pd128(hi);
  ret += _mm_permute_pd(ret, 0b01);
  return ret[0];
}

AVX_TARGET inline double SumOfAbsolute(MatrixComplexDouble2x2 matrix) {
  return std::abs(matrix.Get(0)) + std::abs(matrix.Get(1)) +
         std::abs(matrix.Get(2)) + std::abs(matrix.Get(3));
}

}  // namespace aocommon::avx

#endif  // AOCOMMON_AVX256_MATRIX_COMPLEX_DOUBLE_2X2_H
