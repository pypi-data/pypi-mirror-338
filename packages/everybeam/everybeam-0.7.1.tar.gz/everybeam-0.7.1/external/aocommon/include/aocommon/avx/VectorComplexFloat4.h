// Copyright (C) 2020 ASTRON (Netherlands Institute for Radio Astronomy)
// SPDX-License-Identifier: GPL-3.0-or-later

#ifndef AOCOMMON_AVX_VECTOR_COMPLEX_FLOAT_4_H_
#define AOCOMMON_AVX_VECTOR_COMPLEX_FLOAT_4_H_

#include "AvxMacros.h"
#include "VectorFloat8.h"

#include <cassert>
#include <complex>
#include <immintrin.h>
#include <ostream>

namespace aocommon::avx {

/**
 * Implements a Vector with 4 complex float values.
 * The vector is not initialized by default for performance considerations,
 * a call to Zero() can be used to do that when needed.
 *
 * This class is an implementation detail of
 * @ref aocommon::Avx256::MatrixComplexFloat2x2, but can be used by itself.
 */
class VectorComplexFloat4 {
 public:
  AVX_TARGET VectorComplexFloat4() noexcept = default;

  AVX_TARGET /* implicit */ VectorComplexFloat4(VectorFloat8 data) noexcept
      : data_{data} {}

  AVX_TARGET explicit VectorComplexFloat4(std::complex<float> a,
                                          std::complex<float> b,
                                          std::complex<float> c,
                                          std::complex<float> d) noexcept
      : data_{VectorFloat8{a.real(), a.imag(), b.real(), b.imag(), c.real(),
                           c.imag(), d.real(), d.imag()}} {}

  AVX_TARGET explicit VectorComplexFloat4(
      const std::complex<float> vector[4]) noexcept
      // reinterpret_cast explicitly allowed per [complex.numbers.general]/4.
      // (http://www.eelis.net/c++draft/complex.numbers#general-4)
      : data_{VectorFloat8{
            reinterpret_cast<const float*>(std::addressof(vector[0]))}} {}

  AVX_TARGET explicit VectorComplexFloat4(
      const std::complex<double> vector[4]) noexcept
      // reinterpret_cast explicitly allowed per [complex.numbers.general]/4.
      // (http://www.eelis.net/c++draft/complex.numbers#general-4)
      : data_{VectorFloat8{
            reinterpret_cast<const double*>(std::addressof(vector[0]))}} {}

  AVX_TARGET std::complex<float> Get(size_t index) const noexcept {
    assert(index < 4 && "Index out of bounds.");
    return {data_[2 * index], data_[2 * index + 1]};
  }

  AVX_TARGET void Set(size_t index, std::complex<float> value) noexcept {
    assert(index < 4 && "Index out of bounds.");
    switch (index) {
      case 0:
        *this = VectorComplexFloat4(value, Get(1), Get(2), Get(3));
        break;
      case 1:
        *this = VectorComplexFloat4(Get(0), value, Get(2), Get(3));
        break;
      case 2:
        *this = VectorComplexFloat4(Get(0), Get(1), value, Get(3));
        break;
      case 3:
        *this = VectorComplexFloat4(Get(0), Get(1), Get(2), value);
        break;
    }
  }

  AVX_TARGET explicit operator __m256() const noexcept { return data_.Value(); }

  AVX_TARGET VectorComplexFloat4 Conjugate() const noexcept {
    // Xor-ing a float with  0.0 will not change the value.
    // Xor-ing a float with -0.0 will change the sign of the value.
    __m256 mask = _mm256_setr_ps(0.0, -0.0, 0.0, -0.0, 0.0, -0.0, 0.0, -0.0);
    return data_ ^ mask;
  }

  /** Assign data stored by 4 element complex vector to destination buffer. */
  AVX_TARGET void AssignTo(std::complex<float>* destination) const noexcept {
    data_.AssignTo(reinterpret_cast<float*>(destination));
  }

  AVX_TARGET void AssignTo(std::complex<double>* destination) const noexcept {
    data_.AssignTo(reinterpret_cast<double*>(destination));
  }

  AVX_TARGET static VectorComplexFloat4 Zero() noexcept {
    return VectorComplexFloat4{VectorFloat8::Zero()};
  }

  AVX_TARGET VectorComplexFloat4& operator+=(
      VectorComplexFloat4 value) noexcept {
    data_ += value.data_;
    return *this;
  }

  AVX_TARGET VectorComplexFloat4& operator-=(
      VectorComplexFloat4 value) noexcept {
    data_ -= value.data_;
    return *this;
  }

  AVX_TARGET friend VectorComplexFloat4 operator+(
      VectorComplexFloat4 lhs, VectorComplexFloat4 rhs) noexcept {
    return lhs += rhs;
  }

  AVX_TARGET friend VectorComplexFloat4 operator-(
      VectorComplexFloat4 lhs, VectorComplexFloat4 rhs) noexcept {
    return lhs -= rhs;
  }

  /// Multiplies the elements of 2 vectors in parallel.
  ///
  /// r[0] = lhs[0] * rhs[0]
  /// r[1] = lhs[1] * rhs[1]
  /// r[2] = lhs[2] * rhs[2]
  /// r[3] = lhs[3] * rhs[3]
  AVX_TARGET friend VectorComplexFloat4 operator*(
      VectorComplexFloat4 lhs, VectorComplexFloat4 rhs) noexcept {
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

    // The algorithm could use 512 bit vectors. Since the AVX-512 instruction
    // set isn't widely available the code uses 2 256 bit vectors.

    // lhs    | L0 Re | L0 Im | L1 Re | L1 Im | L2 Re | L2 Im | L3 Re | L3 Im |
    // rhs    | R0 Re | R0 Im | R1 Re | R1 Im | R2 Re | R2 Im | R3 Re | R3 Im |

    __m256 Lv1 =
        _mm256_shuffle_ps(lhs.data_.Value(), lhs.data_.Value(), 0b10'10'00'00);
    __m256 Rv1 =
        _mm256_shuffle_ps(lhs.data_.Value(), lhs.data_.Value(), 0b11'11'01'01);
    __m256 Rv2 =
        _mm256_shuffle_ps(rhs.data_.Value(), rhs.data_.Value(), 0b10'11'00'01);
    __m256 Rv3 = _mm256_mul_ps(Rv1, Rv2);
    return VectorFloat8{_mm256_fmaddsub_ps(Lv1, rhs.data_.Value(), Rv3)};
  }

  AVX_TARGET friend VectorComplexFloat4 operator*(
      VectorComplexFloat4 lhs, std::complex<float> rhs) noexcept {
    return lhs * VectorComplexFloat4{rhs, rhs, rhs, rhs};
  }

  AVX_TARGET friend VectorComplexFloat4 operator*(
      std::complex<float> lhs, VectorComplexFloat4 rhs) noexcept {
    return rhs * lhs;
  }

  AVX_TARGET friend bool operator==(VectorComplexFloat4 lhs,
                                    VectorComplexFloat4 rhs) noexcept {
    return lhs.data_ == rhs.data_;
  }

  AVX_TARGET friend std::ostream& operator<<(std::ostream& output,
                                             VectorComplexFloat4 value) {
    output << '[' << value.Get(0) << ", " << value.Get(1) << ", "
           << value.Get(2) << ", " << value.Get(3) << ']';
    return output;
  }

 private:
  VectorFloat8 data_;
};

}  // namespace aocommon::avx

#endif  // AOCOMMON_AVX256_VECTOR_COMPLEX_FLOAT_4_H
