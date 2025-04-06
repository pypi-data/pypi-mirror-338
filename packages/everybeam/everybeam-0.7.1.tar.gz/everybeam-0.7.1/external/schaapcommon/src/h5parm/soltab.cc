// Copyright (C) 2020 ASTRON (Netherlands Institute for Radio Astronomy)
// SPDX-License-Identifier: GPL-3.0-or-later

#include "soltab.h"

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <ctime>
#include <iomanip>

#include <hdf5.h>

#include "gridinterpolate.h"

// using namespace std;
namespace schaapcommon {
namespace h5parm {

namespace {
std::vector<std::string> Tokenize(const std::string& str,
                                  const std::string& delims) {
  std::vector<std::string> tokens;
  std::string::size_type pos = 0;
  std::string::size_type pos0;

  while ((pos0 = str.find_first_not_of(delims, pos)) != std::string::npos) {
    pos = str.find_first_of(delims, pos0 + 1);
    if (pos - pos0 > 0) {  // If pos == std::string::npos then substr() clamps.
      tokens.push_back(str.substr(pos0, pos - pos0));
    }
  }

  return tokens;
}
}  // namespace

std::vector<double> SelectAxisValues(std::vector<double>&& axis,
                                     double requested_start,
                                     double requested_end, bool nearest,
                                     size_t& start_index) {
  assert(!axis.empty());
  assert(std::is_sorted(axis.cbegin(), axis.cend()));
  assert(requested_start <= requested_end);
  //  ReadAxes() already checked that the time axis is sorted.
  std::vector<double>::const_iterator lower =
      std::lower_bound(axis.cbegin(), axis.cend(), requested_start);
  std::vector<double>::const_iterator upper;
  if (nearest) {
    upper = std::upper_bound(lower, axis.cend(), requested_end);
    // move upper to nearest element
    if (upper > axis.cbegin() && upper != axis.cend()) {
      if (requested_end - *(upper - 1) < *upper - requested_end) {
        --upper;
      }
    }
    // move lower to the nearest element
    if (lower > axis.cbegin()) {
      if (lower == axis.cend() ||
          requested_start - *(lower - 1) < *lower - requested_start) {
        --lower;
      }
    }
  } else {
    upper = std::lower_bound(lower, axis.cend(), requested_end);
    // lower may be larger than the requested value; if this case move lower
    // one value back.
    if (lower > axis.cbegin() &&
        (lower == axis.cend() || *lower > requested_start)) {
      --lower;
    }
  }
  // upper must point to the element after the element that is nearest/bounded:
  if (upper != axis.cend()) {
    ++upper;
  }
  start_index = lower - axis.cbegin();
  axis.assign(lower, upper);
  assert(!axis.empty());
  return std::move(axis);
}

SolTab::SolTab(H5::Group group, const std::string& type,
               const std::vector<AxisInfo>& axes)
    : H5::Group(group), type_(type), axes_(axes) {
  H5::Attribute attr = createAttribute(
      "TITLE", H5::StrType(H5::PredType::C_S1, type_.size()), H5::DataSpace());
  attr.write(H5::StrType(H5::PredType::C_S1, type_.size()), type_);
  AddVersionStamp(*this);
}

SolTab::SolTab(H5::Group& group) : H5::Group(group) {
  // Read the type from the "TITLE" attribute
  if (!attrExists("TITLE")) {
    throw std::runtime_error("H5 attribute TITLE not found in " + GetName());
  }
  H5::Attribute typeattr = openAttribute("TITLE");
  if (typeattr.getDataType().isVariableStr()) {
    throw std::runtime_error(
        "H5Parm attribute TITLE is a variable string, which is not supported");
  }
  hsize_t typenamelen = typeattr.getDataType().getSize();
  std::vector<char> type_chars(typenamelen + 1, '\0');
  typeattr.read(typeattr.getDataType(), type_chars.data());
  type_ = type_chars.data();

  ReadAxes();
}

SolTab::~SolTab() = default;

void SolTab::AddVersionStamp(H5::Group& node) {
  // Write an attribute with the h5parm version
  H5::Attribute attr = node.createAttribute(
      "h5parm_version", H5::StrType(H5::PredType::C_S1, 3), H5::DataSpace());
  attr.write(H5::StrType(H5::PredType::C_S1, 3), "1.0");
}

AxisInfo SolTab::GetAxis(size_t i) const { return axes_[i]; }

AxisInfo SolTab::GetAxis(const std::string& axis_name) const {
  for (const AxisInfo& axis_info : axes_) {
    if (axis_info.name == axis_name) {
      return axis_info;
    }
  }
  throw std::runtime_error("Axis " + axis_name + " does not exist in " +
                           GetName());
}

bool SolTab::HasAxis(const std::string& axis_name) const {
  for (const auto& axis : axes_) {
    if (axis.name == axis_name) return true;
  }
  return false;
}

size_t SolTab::GetAxisIndex(const std::string& axis_name) const {
  for (size_t i = 0; i < axes_.size(); ++i) {
    if (axes_[i].name == axis_name) return i;
  }
  throw std::runtime_error("Axis " + axis_name + " does not exist in " +
                           GetName());
}

void SolTab::SetValues(const std::vector<double>& vals,
                       const std::vector<double>& weights,
                       const std::string& history) {
  // Convert axes to comma separated string, fill dims
  size_t expectedsize = 1;
  std::string axesstr = axes_.front().name;
  std::vector<hsize_t> dims(axes_.size());
  for (size_t i = 0; i < axes_.size(); ++i) {
    dims[i] = axes_[i].size;
    expectedsize *= dims[i];
    if (i > 0) {
      axesstr += "," + axes_[i].name;
    }
  }

  if (expectedsize != vals.size()) {
    throw std::runtime_error(
        "Values for H5Parm do not have the expected size: they have size " +
        std::to_string(vals.size()) + ", expected is " +
        std::to_string(expectedsize));
  }

  H5::DataSpace dataspace(dims.size(), dims.data(), nullptr);
  H5::DataSet dataset =
      createDataSet("val", H5::PredType::IEEE_F64LE, dataspace);

  dataset.write(vals.data(), H5::PredType::IEEE_F64LE);

  H5::Attribute attr = dataset.createAttribute(
      "AXES", H5::StrType(H5::PredType::C_S1, axesstr.size()), H5::DataSpace());
  attr.write(H5::StrType(H5::PredType::C_S1, axesstr.size()), axesstr);

  // Write history if given
  if (history.size() > 0) {
    time_t rawtime;
    struct tm* timeinfo;
    char timebuffer[80];

    time(&rawtime);
    timeinfo = localtime(&rawtime);

    strftime(timebuffer, sizeof(timebuffer), "%d-%m-%Y %H:%M:%S", timeinfo);

    std::string historyline = std::string(timebuffer) + ": " + history;

    H5::StrType historytype =
        H5::StrType(H5::PredType::C_S1, historyline.size());
    H5::Attribute attr =
        dataset.createAttribute("HISTORY000", historytype, H5::DataSpace());
    attr.write(historytype, historyline);
  }

  // Add weights
  // Do not use half float data type because typical weights range can be 1.e-14
  /*
  hid_t halffloat = H5Tcopy(H5T_IEEE_F32BE);
  H5Tset_fields(halffloat, 15, 10, 5, 0, 10);
  H5Tset_size(halffloat, 2);
  H5Tset_ebias(halffloat, 15);
  H5Tlock(halffloat);
  */
  H5::DataSet weightset =
      createDataSet("weight", H5::PredType::IEEE_F32LE, dataspace);

  // If weights are empty, write ones everywhere
  std::vector<double> fullweights;
  if (weights.empty()) {
    fullweights.resize(vals.size(), 1.0);
  } else {
    if (weights.size() != vals.size()) {
      throw std::runtime_error(
          "Values for H5Parm weights do not have the expected size: they have "
          "size " +
          std::to_string(weights.size()) + ", expected is " +
          std::to_string(vals.size()));
    }
    // Copy weights so that they can be changed (to add flags)
    fullweights = weights;
  }

  // Set weight of NaN values to 0.
  for (size_t i = 0; i < vals.size(); ++i) {
    if (std::isnan(vals[i])) {
      fullweights[i] = 0.;
    }
  }

  weightset.write(fullweights.data(), H5::PredType::IEEE_F64LE);

  attr = weightset.createAttribute(
      "AXES", H5::StrType(H5::PredType::C_S1, axesstr.size()), H5::DataSpace());
  attr.write(H5::StrType(H5::PredType::C_S1, axesstr.size()), axesstr);
}

void SolTab::SetComplexValues(const std::vector<std::complex<double>>& values,
                              const std::vector<double>& weights,
                              bool to_amplitudes, const std::string& history) {
  // Convert values to real numbers by taking amplitude or argument.
  std::vector<double> real_values(values.size());

  std::transform(
      values.begin(), values.end(), real_values.begin(),
      to_amplitudes
          ? [](std::complex<double> value) { return std::abs(value); }
          : [](std::complex<double> value) { return std::arg(value); });

  SetValues(real_values, weights, history);
}

void SolTab::ReadAxes() {
  H5::DataSet val;
  try {
    val = openDataSet("val");
  } catch (H5::GroupIException& e) {
    throw std::runtime_error("SolTab " + GetName() + " has no values");
  }

  H5::Attribute axesattr;
  try {
    axesattr = val.openAttribute("AXES");
  } catch (H5::AttributeIException& e) {
    throw std::runtime_error("Values of SolTab " + GetName() +
                             " has no AXES attribute");
  }

  hsize_t axesstrlen = axesattr.getDataType().getSize();
  std::vector<char> axes_chars(axesstrlen + 1, '\0');
  axesattr.read(axesattr.getDataType(), axes_chars.data());
  std::vector<std::string> axesnames = Tokenize(axes_chars.data(), ",");

  const size_t ndims = axesnames.size();

  // Get number of dimensions and size of all dimensions
  H5::DataSpace ds = val.getSpace();
  if (ds.getSimpleExtentNdims() != int(ndims)) {
    throw std::runtime_error(
        "H5Parm is inconsistent: number of axes in data (" +
        std::to_string(ds.getSimpleExtentNdims()) +
        ") does not match number of axes in metadata (" +
        std::to_string(int(ndims)) + ")");
  }
  std::vector<hsize_t> dims_out(ndims, 0);
  ds.getSimpleExtentDims(dims_out.data());

  for (size_t i = 0; i < axesnames.size(); ++i) {
    axes_.push_back(AxisInfo{axesnames[i], dims_out[i]});
  }

  if (HasAxis("time")) {
    const std::vector<double> time_axis = GetRealAxis("time");
    if (!std::is_sorted(time_axis.begin(), time_axis.end())) {
      throw std::runtime_error("Time axis in H5 file should be ordered.");
    }
  }
}

std::string SolTab::GetName() const {
  if (!isValid(getId())) {
    return "<invalid>";
  }
  const ssize_t len = H5Iget_name(getId(), nullptr, 0);
  if (len < 0) {
    throw std::runtime_error("Error retrieving H5 Group name.");
  }
  std::string name(len + 1, '\0');
  H5Iget_name(getId(), name.data(), len + 1);
  // Strip leading /
  return name.data() + 1;
}

std::vector<double> SolTab::GetValues(const std::string& antenna_name,
                                      const std::vector<double>& times,
                                      const std::vector<double>& frequencies,
                                      size_t polarization, size_t direction,
                                      bool nearest) const {
  std::vector<double> values =
      GetValuesOrWeights("val", antenna_name, times, frequencies, polarization,
                         direction, nearest);

  const std::vector<double> weights =
      GetValuesOrWeights("weight", antenna_name, times, frequencies,
                         polarization, direction, nearest);

  ApplyFlags(values, weights);

  return values;
}

std::vector<double> SolTab::GetValuesOrWeights(
    const std::string& val_or_weight, const std::string& antenna_name,
    const std::vector<double>& times, const std::vector<double>& frequencies,
    size_t polarization, size_t direction, bool nearest) const {
  TimesAndFrequencies times_and_frequencies = GetTimesAndFrequencies(
      times, frequencies, polarization, direction, nearest);

  const std::vector<double> sub_array = GetSubArray(
      val_or_weight, antenna_name, times_and_frequencies.start_time_index,
      times_and_frequencies.num_times, 1,
      times_and_frequencies.start_freq_index, times_and_frequencies.num_freqs,
      1, polarization, direction);

  MemoryLayout mem_layout = MemoryLayout::kRowMajor;
  // If the frequency index is lower than the time index, time will be the
  // fastest changing index. The ordering needs to be swapped, to ensure that
  // the frequency will be the fastest changing index
  if (HasAxis("freq") && HasAxis("time") &&
      GetAxisIndex("freq") < GetAxisIndex("time")) {
    mem_layout = MemoryLayout::kColumnMajor;
  }

  return GridNearestNeighbor(times_and_frequencies.time_axis,
                             times_and_frequencies.freq_axis, times,
                             frequencies, sub_array, mem_layout, nearest);
}

void SolTab::ApplyFlags(std::vector<double>& values,
                        const std::vector<double>& weights) {
  assert(values.size() == weights.size());
  for (size_t i = 0; i < values.size(); ++i) {
    if (weights[i] == 0.0) {
      values[i] = std::numeric_limits<double>::quiet_NaN();
    }
  }
}

TimesAndFrequencies SolTab::GetTimesAndFrequencies(
    const std::vector<double>& times, const std::vector<double>& frequencies,
    size_t pol, size_t dir, bool nearest) const {
  assert(!times.empty());
  assert(!frequencies.empty());

  TimesAndFrequencies tf;
  tf.time_axis = {0.0};
  tf.start_time_index = 0;
  tf.freq_axis = {0.0};
  tf.start_freq_index = 0;
  tf.num_freqs = 1;

  if (HasAxis("time")) {
    tf.time_axis = SelectAxisValues(GetRealAxis("time"), times.front(),
                                    times.back(), nearest, tf.start_time_index);
  }
  tf.num_times = tf.time_axis.size();
  if (HasAxis("freq")) {
    std::vector<double> full_freq_axis_h5 = GetRealAxis("freq");
    tf.start_freq_index = GetFreqIndex(frequencies.front());
    tf.num_freqs = GetFreqIndex(frequencies.back()) - tf.start_freq_index + 1;
    tf.freq_axis = std::vector<double>(
        full_freq_axis_h5.begin() + tf.start_freq_index,
        full_freq_axis_h5.begin() + tf.start_freq_index + tf.num_freqs);
  }
  if (HasAxis("pol")) {
    const size_t num_pol_h5 = GetAxis("pol").size;
    if (pol > num_pol_h5 - 1) {
      throw std::runtime_error("Polarization " + std::to_string(pol) +
                               " requested from H5Parm, but only " +
                               std::to_string(num_pol_h5) +
                               " polarizations are in there.");
    }
  }

  return tf;
}

std::vector<double> SolTab::GetSubArray(
    const std::string& val_or_weight, const std::string& antenna_name,
    const size_t start_time_index, const size_t n_times, const size_t time_step,
    const size_t start_freq_index, const size_t n_freqs, const size_t freq_step,
    const size_t polarization, const size_t direction) const {
  std::vector<double> res(n_times * n_freqs);
  H5::DataSet val = openDataSet(val_or_weight);

  // Set offsets and strides
  std::vector<hsize_t> memdims;
  std::vector<hsize_t> offsets;
  std::vector<hsize_t> counts;
  std::vector<hsize_t> strides;
  memdims.reserve(axes_.size());
  offsets.reserve(axes_.size());
  counts.reserve(axes_.size());
  strides.reserve(axes_.size());

  for (const AxisInfo& axis_info : axes_) {
    hsize_t stride = 1;
    hsize_t count = 1;
    hsize_t memdim = 1;
    hsize_t offset = 0;
    if (axis_info.name == "time") {
      offset = start_time_index;
      stride = time_step;
      count = n_times;
      memdim = n_times;
    } else if (axis_info.name == "freq") {
      offset = start_freq_index;
      stride = freq_step;
      count = n_freqs;
      memdim = n_freqs;
    } else if (axis_info.name == "ant") {
      offset = GetAntIndex(antenna_name);
    } else if (axis_info.name == "dir") {
      offset = direction;
    } else if (axis_info.name == "pol") {
      offset = polarization;
    } else if (axis_info.size != 1) {
      throw std::runtime_error("Axis \"" + axis_info.name +
                               "\" in H5Parm is not understood");
    }
    memdims.push_back(memdim);
    offsets.push_back(offset);
    counts.push_back(count);
    strides.push_back(stride);
  }

  H5::DataSpace dataspace = val.getSpace();

  dataspace.selectHyperslab(H5S_SELECT_SET, counts.data(), offsets.data(),
                            strides.data());

  // Setup memory dataspace
  H5::DataSpace memspace(axes_.size(), memdims.data());
  try {
    val.read(res.data(), H5::PredType::NATIVE_DOUBLE, memspace, dataspace);
  } catch (H5::DataSetIException& e) {
    e.printErrorStack();
    throw std::runtime_error("Could not read data");
  }
  return res;
}

std::vector<double> SolTab::GetCompleteArray(
    const std::string& value_or_weight, const size_t n_axes,
    const std::array<size_t, 5>& size_axis) const {
  std::vector<hsize_t> memory_dimensions;
  std::vector<hsize_t> offsets;
  std::vector<hsize_t> counts;
  std::vector<hsize_t> strides;
  size_t result_size = 1;

  for (size_t i = 0; i < n_axes; i++) {
    memory_dimensions.push_back(size_axis[i]);
    offsets.push_back(0);
    counts.push_back(size_axis[i]);
    strides.push_back(1);
    result_size *= size_axis[i];
  }

  std::vector<double> result(result_size);
  H5::DataSet val = openDataSet(value_or_weight);
  H5::DataSpace dataspace = val.getSpace();
  dataspace.selectHyperslab(H5S_SELECT_SET, counts.data(), offsets.data(),
                            strides.data());
  // Setup memory dataspace
  H5::DataSpace memory_space(n_axes, memory_dimensions.data());
  try {
    val.read(result.data(), H5::PredType::NATIVE_DOUBLE, memory_space,
             dataspace);
  } catch (H5::DataSetIException& e) {
    e.printErrorStack();
    throw std::runtime_error("Could not read data");
  }

  return result;
}

void SolTab::SetAntennas(const std::vector<std::string>& sol_antennas) {
  // TODO: check that antenna is present in antenna table in solset
  std::array<hsize_t, 1> dimensions{{sol_antennas.size()}};

  size_t str_max_length = 1;
  for (const std::string& name : sol_antennas) {
    str_max_length = std::max(str_max_length, name.length());
  }

  if (nameExists("ant")) unlink("ant");

  // Create dataset
  H5::DataSpace dataspace(dimensions.size(), dimensions.data(), nullptr);
  H5::DataType datatype = H5::StrType(H5::PredType::C_S1, str_max_length);
  H5::DataSet dataset = createDataSet("ant", datatype, dataspace);

  // Prepare data
  std::vector<char> ant_array(sol_antennas.size() * str_max_length);
  char* ant_array_position = ant_array.data();
  for (const std::string& antenna_name : sol_antennas) {
    strncpy(ant_array_position, antenna_name.c_str(), str_max_length);
    ant_array_position += str_max_length;
  }

  dataset.write(ant_array.data(), datatype);

  // Update cache
  ant_list_ = sol_antennas;
  ant_map_.clear();
  for (size_t i = 0; i < sol_antennas.size(); ++i) {
    ant_map_[sol_antennas[i]] = i;
  }
}

void SolTab::SetAxisMeta(const std::string& meta_name, size_t num_char,
                         const std::vector<std::string>& meta_vals) {
  hsize_t dims[1];  // Only a name
  dims[0] = meta_vals.size();

  // Create dataset
  H5::DataSpace dataspace(1, dims, nullptr);
  H5::DataSet dataset = createDataSet(
      meta_name, H5::StrType(H5::PredType::C_S1, num_char), dataspace);

  if (meta_vals.size() > 0) {
    // Prepare data
    std::vector<char> src_array(meta_vals.size() * num_char);
    char* src_array_position = src_array.data();
    for (const std::string& meta_value : meta_vals) {
      strncpy(src_array_position, meta_value.c_str(), num_char);
      src_array_position += num_char;
    }

    dataset.write(src_array.data(), H5::StrType(H5::PredType::C_S1, num_char));
  }
}

void SolTab::SetSources(const std::vector<std::string>& sol_sources) {
  SetAxisMeta("dir", 128, sol_sources);
}

void SolTab::SetPolarizations(const std::vector<std::string>& polarizations) {
  SetAxisMeta("pol", 2, polarizations);
}

void SolTab::SetFreqs(const std::vector<double>& freqs) {
  SetAxisMeta("freq", freqs);
}

void SolTab::SetTimes(const std::vector<double>& times) {
  SetAxisMeta("time", times);
}

void SolTab::SetAxisMeta(const std::string& meta_name,
                         const std::vector<double>& meta_vals) {
  hsize_t dims[1];
  dims[0] = meta_vals.size();

  // Create dataset
  H5::DataSpace dataspace(1, dims, nullptr);
  H5::DataSet dataset =
      createDataSet(meta_name, H5::PredType::IEEE_F64LE, dataspace);

  if (meta_vals.size() > 0) {
    dataset.write(meta_vals.data(), H5::PredType::IEEE_F64LE);
  }
}

void SolTab::FillCache(std::vector<std::string>& list,
                       std::map<std::string, hsize_t>& map,
                       const std::string& table_name) const {
  if (!list.empty()) return;
  assert(map.empty());
  map.clear();  // Just in case.

  H5::DataSet dataset;
  H5::DataSpace dataspace;
  try {
    dataset = openDataSet(table_name);
    dataspace = dataset.getSpace();
  } catch (H5::GroupIException& e) {
    throw std::runtime_error("SolTab has no table " + table_name);
  }
  if (dataspace.getSimpleExtentNdims() != 1) {
    throw std::runtime_error("Invalid H5Parm: table \"" + table_name +
                             "\" should be onedimensional");
  }
  hsize_t dims[1];
  dataspace.getSimpleExtentDims(dims);

  // TODO: check that DataType is String
  hsize_t str_len = dataset.getDataType().getSize();

  // Add 1 to the vector length, since the loop below modifies that element
  // in its last iteration.
  std::vector<char> el_names(str_len * dims[0] + 1, '\0');
  dataset.read(el_names.data(), H5::StrType(H5::PredType::C_S1, str_len));

  // Store the names in 'list' in their original order, for GetStringAxis.
  // Also, map the names to their original index in 'map', for GetAntIndex and
  // GetDirIndex.
  list.reserve(dims[0]);
  for (hsize_t el_num = 0; el_num < dims[0]; ++el_num) {
    const size_t name_index = el_num * str_len;
    const size_t next_index = name_index + str_len;
    const char saved = el_names[next_index];
    el_names[next_index] = '\0';
    list.emplace_back(&el_names[name_index]);
    map[list.back()] = el_num;
    el_names[next_index] = saved;
  }
}

hsize_t SolTab::GetNamedIndex(std::vector<std::string>& cache_list,
                              std::map<std::string, hsize_t>& cache_map,
                              const std::string& table_name,
                              const std::string& element_name) const {
  // Initialize ant_list_+ant_map_ or dir_list_+dir_map_ on first use.
  FillCache(cache_list, cache_map, table_name);

  auto it = cache_map.find(element_name);
  if (it == cache_map.end()) {
    throw std::runtime_error("SolTab has no element " + element_name + " in " +
                             table_name);
  }
  return it->second;
}

hsize_t SolTab::GetAntIndex(const std::string& ant_name) const {
  return GetNamedIndex(ant_list_, ant_map_, "ant", ant_name);
}

hsize_t SolTab::GetDirIndex(const std::string& direction_name) const {
  return GetNamedIndex(dir_list_, dir_map_, "dir", direction_name);
}

hsize_t SolTab::GetFreqIndex(double freq) const {
  if (GetAxis("freq").size == 1) {
    return 0;
  }
  std::vector<double> freqs = GetRealAxis("freq");
  double freq_interval = GetFreqInterval(0);

  // A full cell width before the first frequency
  if (freq < freqs.front() - freq_interval) {
    throw std::runtime_error("Frequency " + std::to_string(freq) +
                             " not found in " + GetName());
  }
  if (freq < freqs.front()) {
    return 0;
  }
  // No assumptions on regular spacing here
  for (size_t i = 0; i < freqs.size() - 1; ++i) {
    if (freq < freqs[i + 1]) {
      // Nearest neighbor: i or i+1
      if (freq - freqs[i] < freqs[i + 1] - freq) {
        return i;
      } else {
        return i + 1;
      }
    }
  }

  // A full cell width after the last frequency
  freq_interval = GetFreqInterval(freqs.size() - 2);
  if (freq < freqs.back() + freq_interval) {
    return freqs.size() - 1;
  }

  throw std::runtime_error("Frequency " + std::to_string(freq) +
                           " not found in " + GetName());
  return 0;
}

std::vector<double> SolTab::GetRealAxis(const std::string& axisname) const {
  H5::DataSet dataset;
  H5::DataSpace dataspace;
  try {
    dataset = openDataSet(axisname);
    dataspace = dataset.getSpace();
  } catch (H5::GroupIException& e) {
    throw std::runtime_error("SolTab " + GetName() + " has no axis '" +
                             axisname + "'");
  }
  if (dataspace.getSimpleExtentNdims() != 1) {
    throw std::runtime_error(
        "Error in H5Parm: dataspace.getSimpleExtentNdims() = " +
        std::to_string(dataspace.getSimpleExtentNdims()) + " for axis " +
        axisname + ", this should be a one-dimensional array");
  }

  hsize_t dims[1];
  dataspace.getSimpleExtentDims(dims);

  std::vector<double> data(dims[0]);
  dataset.read(data.data(), H5::PredType::NATIVE_DOUBLE);

  return data;
}

const std::vector<std::string>& SolTab::GetStringAxis(
    const std::string& axis_name) const {
  if (axis_name == "dir") {
    FillCache(dir_list_, dir_map_, "dir");
    return dir_list_;
  } else if (axis_name == "ant") {
    FillCache(ant_list_, ant_map_, "ant");
    return ant_list_;
  } else if (axis_name == "pol") {
    FillCache(pol_list_, pol_map_, "pol");
    return pol_list_;
  } else {
    throw std::runtime_error(
        "Only string axes 'ant', 'dir' and 'pol' supported for now.");
  }
}

hsize_t SolTab::GetTimeIndex(double time) const {
  if (GetAxis("time").size == 1) {
    return 0;
  }
  std::vector<double> times = GetRealAxis("time");

  double timeInterval = GetTimeInterval();

  for (size_t i = 0; i < times.size(); ++i) {
    if (std::abs(times[i] - time) <
        timeInterval * 0.501) {  // 0.5 with some tolerance
      return i;
    }
  }
  throw std::runtime_error("Time " + std::to_string(time) + " not found in " +
                           GetName());
  return 0;
}

double SolTab::GetInterval(const std::string& axis_name, size_t start) const {
  H5::DataSet dataset;
  H5::DataSpace dataspace;
  try {
    dataset = openDataSet(axis_name);
    dataspace = dataset.getSpace();
  } catch (H5::GroupIException& e) {
    throw std::runtime_error("SolTab " + GetName() + " has no axis table for " +
                             axis_name);
  }
  if (dataspace.getSimpleExtentNdims() != 1) {
    throw std::runtime_error("Invalid H5Parm: table \"" + axis_name +
                             "\" should be onedimensional");
  }

  hsize_t dims[1];
  dataspace.getSimpleExtentDims(dims);
  if (dims[0] <= start + 1) {
    throw std::runtime_error("For reading the " + axis_name +
                             " interval, more than one value is required.");
  }

  hsize_t count[1], offset[1], memoffset[1];
  count[0] = 2;
  offset[0] = start;
  memoffset[0] = 0;
  dataspace.selectHyperslab(H5S_SELECT_SET, count, offset);

  H5::DataSpace memspace(1, count);
  memspace.selectHyperslab(H5S_SELECT_SET, count, memoffset);

  // Get only two values
  double values[2];
  dataset.read(&values, H5::PredType::NATIVE_DOUBLE, memspace, dataspace);
  return values[1] - values[0];
}
}  // namespace h5parm
}  // namespace schaapcommon
