// Copyright (C) 2020 ASTRON (Netherlands Institute for Radio Astronomy)
// SPDX-License-Identifier: GPL-3.0-or-later

#include "h5parm.h"

#include <array>
#include <cstring>
#include <complex>
#include <sstream>
#include <iomanip>
#include <sys/stat.h>
#include <limits>
#include <cstddef>

#include <hdf5.h>
#include <iostream>

#include <aocommon/imagecoordinates.h>

#include "h5cache.h"

#ifndef offsetof
#error offsetof not supported by your compiler.
#endif

namespace schaapcommon {
namespace h5parm {
H5Parm::H5Parm(const std::string& filename, bool force_new,
               bool force_new_sol_set, const std::string& sol_set_name)
    : H5::H5File(filename, force_new ? H5F_ACC_TRUNC : H5F_ACC_RDONLY) {
  if (force_new_sol_set || getNumObjs() == 0) {  // Create a new solSet
    if (sol_set_name == "") {
      // Get the name of first non-existing solset
      std::stringstream new_sol_set_name;
      H5::Group try_group;
      for (size_t sol_set_idx = 0; sol_set_idx < 100; ++sol_set_idx) {
        try {
          H5::Exception::dontPrint();
          new_sol_set_name << "sol" << std::setfill('0') << std::setw(3)
                           << sol_set_idx;
          try_group = openGroup(new_sol_set_name.str());
          new_sol_set_name.str("");
        } catch (H5::FileIException& not_found_error) {
          // sol_set_name does not exist yet
          break;
        }
        try_group.close();
      }
      sol_set_ = createGroup("/" + new_sol_set_name.str(), H5P_DEFAULT);
    } else {
      // Create solset with the given name
      sol_set_ = createGroup("/" + sol_set_name, H5P_DEFAULT);
    }
    AddVersionStamp(sol_set_);
  } else {
    std::string sol_set_name_to_open = sol_set_name;
    if (sol_set_name_to_open == "") {
      if (this->getNumObjs() == 1) {
        sol_set_name_to_open = this->getObjnameByIdx(0);
      } else {
        throw std::runtime_error("H5Parm " + filename +
                                 " contains more than one SolSet, " +
                                 "please specify which one to use.");
      }
    }

    sol_set_ = openGroup(sol_set_name_to_open);

    std::vector<std::string> sol_tab_names;
    for (size_t i = 0; i < sol_set_.getNumObjs(); ++i) {
      if (sol_set_.getObjTypeByIdx(i) == H5G_GROUP) {
        sol_tab_names.push_back(sol_set_.getObjnameByIdx(i));
      }
    }

    for (const std::string& sol_tab_name : sol_tab_names) {
      H5::Group group = sol_set_.openGroup(sol_tab_name);
      sol_tabs_.emplace(sol_tab_name, std::make_unique<SolTab>(group));
    }
  }
}

H5Parm::H5Parm(const std::string& filename,
               const std::vector<std::string>& tables_in_cache)
    : H5::H5File(filename, H5F_ACC_RDONLY) {
  using schaapcommon::h5parm::H5Cache;

  if (getNumObjs() > 0) {
    std::string sol_set_name_to_open;
    if (this->getNumObjs() == 1) {
      sol_set_name_to_open = this->getObjnameByIdx(0);
    } else {
      throw std::runtime_error(
          "H5Parm " + filename + " contains more than one SolSet. " +
          "When using caching, only one SolSet is supported.");
    }

    sol_set_ = openGroup(sol_set_name_to_open);

    std::vector<std::string> sol_tab_names;
    for (size_t i = 0; i < sol_set_.getNumObjs(); ++i) {
      if (sol_set_.getObjTypeByIdx(i) == H5G_GROUP) {
        sol_tab_names.push_back(sol_set_.getObjnameByIdx(i));
      }
    }

    // Check that every table name in tables_in_cache is valid.
    for (const std::string& table_cache : tables_in_cache) {
      if (std::find(sol_tab_names.begin(), sol_tab_names.end(), table_cache) ==
          sol_tab_names.end()) {
        throw std::runtime_error("'" + table_cache +
                                 "' does not exist in solset " +
                                 GetSolSetName());
      }
    }

    for (const std::string& sol_tab_name : sol_tab_names) {
      H5::Group group = sol_set_.openGroup(sol_tab_name);

      // If sol_tab_name is included in the tables_in_cache,
      // then it creates a H5Cache, otherwise a SolTab.
      std::unique_ptr<SolTab> sol_tab;
      if (std::find(tables_in_cache.begin(), tables_in_cache.end(),
                    sol_tab_name) != tables_in_cache.end()) {
        sol_tab = std::make_unique<H5Cache>(group);
      } else {
        sol_tab = std::make_unique<SolTab>(group);
      }
      sol_tabs_.emplace(sol_tab_name, std::move(sol_tab));
    }
  }
}

H5Parm::H5Parm() = default;

H5Parm::~H5Parm() {
  // Throw compile time assertion if source_t or antenna_t don't have
  // standard layout
  static_assert(std::is_standard_layout<source_t>::value,
                "source_t doesn't have standard layout");
  static_assert(std::is_standard_layout<antenna_t>::value,
                "antenna_t doesn't have standard layout");
  sol_set_.close();
}

std::string H5Parm::GetSolSetName() const {
  char buffer[100];
  hsize_t namelen = H5Iget_name(sol_set_.getId(), buffer, 100);
  buffer[namelen + 1] = 0;
  // Strip leading '/'
  return buffer + 1;
}

void H5Parm::AddSources(const std::vector<std::string>& names,
                        const std::vector<std::pair<double, double>>& dirs) {
  hsize_t dims[1];

  // Create data type
  dims[0] = 2;  // For ra, dec in directions
  H5::CompType source_type(sizeof(source_t));
  source_type.insertMember("name", offsetof(source_t, name),
                           H5::StrType(H5::PredType::C_S1, 128));
  source_type.insertMember("dir", offsetof(source_t, dir),
                           H5::ArrayType(H5::PredType::NATIVE_DOUBLE, 1, dims));

  // Create dataset
  dims[0] = names.size();
  H5::DataSpace dataspace(1, dims, nullptr);
  H5::DataSet dataset =
      sol_set_.createDataSet("source", source_type, dataspace);

  // Prepare data
  std::vector<source_t> sources(names.size());
  for (size_t src = 0; src < sources.size(); ++src) {
    std::strncpy(sources[src].name, names[src].c_str(), 127);
    sources[src].name[127] = 0;
    sources[src].dir[0] = dirs[src].first;
    sources[src].dir[1] = dirs[src].second;
  }

  // Write data
  dataset.write(&(sources[0]), source_type);
}

void H5Parm::AddAntennas(const std::vector<std::string>& names,
                         const std::vector<std::array<double, 3>>& positions) {
  hsize_t dims[1];

  // Create data type
  dims[0] = 3;  // For x,y,z in positions
  H5::CompType antenna_type(sizeof(antenna_t));
  antenna_type.insertMember("name", offsetof(antenna_t, name),
                            H5::StrType(H5::PredType::C_S1, 16));
  antenna_type.insertMember("position", offsetof(antenna_t, position),
                            H5::ArrayType(H5::PredType::NATIVE_FLOAT, 1, dims));

  // Create dataset
  dims[0] = names.size();
  H5::DataSpace dataspace(1, dims, nullptr);
  H5::DataSet dataset =
      sol_set_.createDataSet("antenna", antenna_type, dataspace);

  // Prepare data
  std::vector<antenna_t> ants(names.size());
  for (size_t ant = 0; ant < ants.size(); ++ant) {
    std::strncpy(ants[ant].name, names[ant].c_str(), 15);
    ants[ant].name[15] = 0;
    const std::array<double, 3>& pos = positions[ant];
    ants[ant].position[0] = pos[0];
    ants[ant].position[1] = pos[1];
    ants[ant].position[2] = pos[2];
  }

  dataset.write(&(ants[0]), antenna_type);
}

SolTab& H5Parm::GetSolTab(const std::string& name) {
  decltype(sol_tabs_)::iterator item_sol_tab = sol_tabs_.find(name);
  if (item_sol_tab == sol_tabs_.end()) {
    throw std::runtime_error("SolTab " + name + " does not exist in solset " +
                             GetSolSetName());
  }
  return *item_sol_tab->second;
}

bool H5Parm::HasSolTab(const std::string& sol_tab_name) const {
  return sol_tabs_.find(sol_tab_name) != sol_tabs_.end();
}

SolTab& H5Parm::CreateSolTab(const std::string& name, const std::string& type,
                             const std::vector<AxisInfo>& axes) {
  H5::Group newgroup = sol_set_.createGroup(name);
  auto sol_tab = std::make_unique<SolTab>(newgroup, type, axes);
  decltype(sol_tabs_)::iterator new_item =
      sol_tabs_.emplace(name, std::move(sol_tab)).first;
  return *new_item->second;
}

size_t H5Parm::GetNumSources() const {
  std::vector<source_t> sources = ReadSourceTable(sol_set_);
  return sources.size();
}

std::vector<H5Parm::source_t> H5Parm::GetSources() const {
  std::vector<source_t> sources = ReadSourceTable(sol_set_);
  return sources;
}

std::string H5Parm::GetNearestSource(double ra, double dec) const {
  std::vector<source_t> sources = ReadSourceTable(sol_set_);

  std::string dirname;
  double min_dist = std::numeric_limits<double>::max();
  for (const source_t& val : sources) {
    const double current_dist =
        aocommon::ImageCoordinates::AngularDistance<double>(ra, dec, val.dir[0],
                                                            val.dir[1]);
    if (current_dist < min_dist) {
      dirname = val.name;
      min_dist = current_dist;
    }
  }
  return dirname;
}

bool H5Parm::IsThreadSafe() {
  hbool_t is_thread_safe = false;
  H5is_library_threadsafe(&is_thread_safe);
  return is_thread_safe;
}

std::vector<H5Parm::source_t> H5Parm::ReadSourceTable(
    const H5::Group& sol_set) const {
  H5::DataSet dataset;
  H5::DataSpace dataspace;
  try {
    dataset = sol_set.openDataSet("source");
    dataspace = dataset.getSpace();
  } catch (H5::GroupIException& e) {
    throw std::runtime_error("H5 file contains no dataset 'source'");
  }

  hsize_t dims[1];
  dataspace.getSimpleExtentDims(dims);
  std::vector<source_t> sources(dims[0]);

  // Create compound data type
  // Inferring this from the dataset with getDataType()
  // leads to unexpected errors.
  const hsize_t npdims[1] = {2};  // Should store ra, dec
  H5::CompType source_type(sizeof(source_t));
  source_type.insertMember("name", offsetof(source_t, name),
                           H5::StrType(H5::PredType::C_S1, 128));
  source_type.insertMember(
      "dir", offsetof(source_t, dir),
      H5::ArrayType(H5::PredType::NATIVE_DOUBLE, 1, npdims));
  dataset.read(sources.data(), source_type);
  return sources;
}

}  // namespace h5parm
}  // namespace schaapcommon
