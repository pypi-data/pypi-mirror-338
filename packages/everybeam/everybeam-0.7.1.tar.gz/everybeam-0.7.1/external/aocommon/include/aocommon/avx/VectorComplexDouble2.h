// Copyright (C) 2020 ASTRON (Netherlands Institute for Radio Astronomy)
// SPDX-License-Identifier: GPL-3.0-or-later

#ifndef AOCOMMON_AVX256_VECTOR_COMPLEX_DOUBLE_2_H
#define AOCOMMON_AVX256_VECTOR_COMPLEX_DOUBLE_2_H

#include "VectorDouble4.h"

#include <algorithm>
#include <cassert>
#include <complex>
#include <immintrin.h>
#include <ostream>

namespace aocommon::avx {

/**
 * Implements a Vector with 2 complex double values.
 * The vector is not initialized by default for performance considerations,
 * a call to Zero() can be used to do that when needed.
 *
 * This class is an implementation detail of
 * @ref aocommon::Avx256::MatrixComplexDouble2x2, but can be used by itself.
 */
class VectorComplexDouble2 {
 public:
  AVX_TARGET VectorComplexDouble2() noexcept = default;

  AVX_TARGET VectorComplexDouble2(const VectorComplexDouble2&) noexcept =
      default;
  AVX_TARGET VectorComplexDouble2& operator=(
      const VectorComplexDouble2&) noexcept = default;

  AVX_TARGET /* implicit */ VectorComplexDouble2(VectorDouble4 data) noexcept
      : data_{data} {}

  AVX_TARGET explicit VectorComplexDouble2(std::complex<double> a,
                                           std::complex<double> b) noexcept
      : data_{VectorDouble4{a.real(), a.imag(), b.real(), b.imag()}} {}

  AVX_TARGET explicit VectorComplexDouble2(
      const std::complex<float> vector[2]) noexcept
      // reinterpret_cast explicitly allowed per [complex.numbers.general]/4.
      // (http://www.eelis.net/c++draft/complex.numbers#general-4)
      : data_{VectorDouble4{
            reinterpret_cast<const float*>(std::addressof(vector[0]))}} {}

  AVX_TARGET explicit VectorComplexDouble2(
      const std::complex<double> vector[2]) noexcept
      // reinterpret_cast explicitly allowed per [complex.numbers.general]/4.
      // (http://www.eelis.net/c++draft/complex.numbers#general-4)
      : data_{VectorDouble4{
            reinterpret_cast<const double*>(std::addressof(vector[0]))}} {}

  AVX_TARGET std::complex<double> Get(size_t index) const noexcept {
    assert(index < 2 && "Index out of bounds.");
    return {data_[2 * index], data_[2 * index + 1]};
  }

  AVX_TARGET void Set(size_t index, std::complex<double> value) noexcept {
    assert(index < 2 && "Index out of bounds.");
    if (index == 0)
      data_ = VectorDouble4(value.real(), value.imag(), Get(1).real(),
                            Get(1).imag());
    else
      data_ = VectorDouble4(Get(0).real(), Get(0).imag(), value.real(),
                            value.imag());
  }

  AVX_TARGET explicit operator __m256d() const noexcept {
    return data_.Value();
  }

  AVX_TARGET VectorComplexDouble2 Conjugate() const noexcept {
    // Xor-ing a double with  0.0 will not change the value.
    // Xor-ing a double with -0.0 will change the sign of the value.
    __m256d mask = _mm256_setr_pd(0.0, -0.0, 0.0, -0.0);
    return data_ ^ mask;
  }

  /** Assign data stored by 2 element complex vector to destination buffer */
  AVX_TARGET void AssignTo(std::complex<double>* destination) const noexcept {
    data_.AssignTo(reinterpret_cast<double*>(destination));
  }

  AVX_TARGET void AssignTo(std::complex<float>* destination) const noexcept {
    std::complex<double> values[2];
    data_.AssignTo(reinterpret_cast<double*>(values));
    std::copy_n(values, 2, destination);
  }

  AVX_TARGET static VectorComplexDouble2 Zero() noexcept {
    return VectorComplexDouble2{VectorDouble4::Zero()};
  }

  AVX_TARGET VectorComplexDouble2& operator+=(
      VectorComplexDouble2 value) noexcept {
    data_ += value.data_;
    return *this;
  }

  AVX_TARGET VectorComplexDouble2& operator-=(
      VectorComplexDouble2 value) noexcept {
    data_ -= value.data_;
    return *this;
  }

  AVX_TARGET friend VectorComplexDouble2 operator+(
      VectorComplexDouble2 lhs, VectorComplexDouble2 rhs) noexcept {
    return lhs += rhs;
  }

  AVX_TARGET friend VectorComplexDouble2 operator-(
      VectorComplexDouble2 lhs, VectorComplexDouble2 rhs) noexcept {
    return lhs -= rhs;
  }

  /// Multiplies the elements of 2 vectors on parallel.
  ///
  /// r[0] = lhs[0] * rhs[0]
  /// r[1] = lhs[1] * rhs[1]
  AVX_TARGET friend VectorComplexDouble2 operator*(
      VectorComplexDouble2 lhs, VectorComplexDouble2 rhs) noexcept {
    // The complex multiplication L * R is performed by:
    // L * R = (L Re * R Re) - (L Im * R Im) +
    //        ((L Re * R Im) + (L Im * R Re)) i

    // Transformed for AVX this becomes
    //
    // mul 1:
    //
    // Lv1 | L Re        | L Re        |
    // Lv2 | R Re        | R Im        | Note this is rhs
    //     ------------- * ----------- *
    // Lv3 | L Re * R Re | L Re * R Im |
    //
    // mul 2:
    //
    // Rv1 | L Im        | L Im        |
    // Rv2 | R Im        | R Re        |
    //     ------------- * ----------- *
    // Rv3 | L Im * R Im | L Im * R Re |
    //
    // add sub
    // Lv3 | L Re * R Re               | L Re * R Im               |
    // Rv3 | L Im * R Im               | L Im * R Re               |
    //     --------------------------- - ------------------------- +
    //     | L Re * R Re - L Im * R Im | L Re * R Im + L Im * R Re |
    //
    // It's also possible to do an fmul add sub
    // Which does (Lv1 fmul Lv2) add/sub Rv3

    // The algorithm "uses" 512 bit vectors. Since the AVX-512 instruction set
    // isn't widely available the code uses 2 256 bit vectors.

    // lhs    | L0 Re | L0 Im | L1 Re | L1 Im |

    __m256d Rv1 =
        _mm256_shuffle_pd(lhs.data_.Value(), lhs.data_.Value(), 0b11'11);
    __m256d Rv2 =
        _mm256_shuffle_pd(rhs.data_.Value(), rhs.data_.Value(), 0b01'01);
    __m256d Rv3 = _mm256_mul_pd(Rv1, Rv2);
    __m256d Lv1 =
        _mm256_shuffle_pd(lhs.data_.Value(), lhs.data_.Value(), 0b00'00);
    return VectorDouble4{_mm256_fmaddsub_pd(Lv1, rhs.data_.Value(), Rv3)};
  }

  AVX_TARGET friend VectorComplexDouble2 operator*(
      VectorComplexDouble2 lhs, std::complex<double> rhs) noexcept {
    return lhs * VectorComplexDouble2{rhs, rhs};
  }

  AVX_TARGET friend VectorComplexDouble2 operator*(
      std::complex<double> lhs, VectorComplexDouble2 rhs) noexcept {
    return rhs * lhs;
  }

  AVX_TARGET friend bool operator==(VectorComplexDouble2 lhs,
                                    VectorComplexDouble2 rhs) noexcept {
    return lhs.data_ == rhs.data_;
  }

  AVX_TARGET friend std::ostream& operator<<(std::ostream& output,
                                             VectorComplexDouble2 value) {
    output << '[' << value.Get(0) << ", " << value.Get(1) << ']';
    return output;
  }

 private:
  VectorDouble4 data_;
};

}  // namespace aocommon::avx

#endif  // AOCOMMON_AVX256_VECTOR_COMPLEX_DOUBLE_2_H
