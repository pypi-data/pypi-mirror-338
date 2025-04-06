#ifndef AOCOMMON_THROWRUNTIMEERROR_H_
#define AOCOMMON_THROWRUNTIMEERROR_H_

#include <sstream>
#include <stdexcept>

namespace aocommon {

#if __cplusplus < 201703L
namespace detail {

inline void Stream(std::stringstream&) {}

template <class T, class... Args>
void Stream(std::stringstream& sstr, const T& value, const Args&... args) {
  sstr << value;
  Stream(sstr, args...);
}
}  // namespace detail
#endif

/**
 * Helper function to throw a @c std::runtime_error.
 *
 * The function concatenates the @a args to a string and uses that message as
 * error message for the exception.
 */
template <class... Args>
[[noreturn]] void ThrowRuntimeError(const Args&... args) {
  std::stringstream sstr;
#if __cplusplus > 201402L
  ((sstr << args), ...);
#else
  detail::Stream(sstr, args...);
#endif
  throw std::runtime_error(sstr.str());
}

}  // namespace aocommon

#endif  // AO_THROW_RUNTIME_ERROR_H
