#ifndef AOCOMMON_BANDDATA_H_
#define AOCOMMON_BANDDATA_H_

#include "uvector.h"

#include <stdexcept>

#include <casacore/ms/MeasurementSets/MeasurementSet.h>

#include <casacore/tables/Tables/ArrayColumn.h>
#include <casacore/tables/Tables/ScalarColumn.h>

namespace aocommon {

/** Global function that returns the speed of light in meters per second. */
constexpr static long double c() { return 299792458.0L; }

/** Holds the meta data of a channel. */
class ChannelInfo {
 public:
  /** Construct a channel.
   * @param frequency Channel frequency in Hz.
   * @param width Channel width in Hz.
   */
  constexpr ChannelInfo(double frequency, double width)
      : _frequency(frequency), _width(width) {}

  /** Whether the frequency of the lhs is less than that of the rhs.
   * @param rhs ChannelInfo to compare with.
   * @returns lhs.Frequency() < rhs.Frequency()
   */
  constexpr bool operator<(const ChannelInfo& rhs) const {
    return _frequency < rhs._frequency;
  }

  /** Whether the frequency of the lhs is greater than that of the rhs.
   * @param rhs ChannelInfo to compare with.
   * @returns lhs.Frequency() > rhs.Frequency()
   */
  constexpr bool operator>(const ChannelInfo& rhs) const {
    return _frequency > rhs._frequency;
  }

  /** Whether the frequencies of lhs and rhs are the same. The channel width is
   * ignored.
   * @param rhs ChannelInfo to compare with
   * @returns lhs.Frequency() == rhs.Frequency()
   */
  constexpr bool operator==(const ChannelInfo& rhs) const {
    return _frequency == rhs._frequency;
  }

  /** Frequency of channel in Hz. */
  constexpr double Frequency() const { return _frequency; }
  /** Width of channel in Hz. */
  constexpr double Width() const { return _width; }

 private:
  double _frequency, _width;
};

/**
 * Contains information about a single band ("spectral window").
 * A band consists of a sequence of contiguous channels.
 */
class BandData {
 public:
  /** Reverse iterator of frequencies */
  typedef std::reverse_iterator<double*> reverse_iterator;
  /** Constant reverse iterator of frequencies. */
  typedef std::reverse_iterator<const double*> const_reverse_iterator;

  /**
   * Construct an empty instance.
   */
  BandData()
      : _channelCount(0),
        _channelFrequencies(),
        _frequencyStep(0.0),
        _referenceFrequency(0.0) {}

  /**
   * Construct an instance from a spectral window table. The spectral window
   * table can only have a single entry, otherwise an exception is thrown.
   * @param spwTable The CASA Measurement Set spectral window table.
   */
  explicit BandData(const casacore::MSSpectralWindow& spwTable) {
    if (spwTable.nrow() != 1)
      throw std::runtime_error("Set should have exactly one spectral window");

    initFromTable(spwTable, 0);
  }

  /**
   * Construct an instance from a specified entry of a spectral window table.
   * @param spwTable The CASA Measurement Set spectral window table.
   * @param bandIndex The entry index of the spectral window table.
   */
  BandData(const casacore::MSSpectralWindow& spwTable, size_t bandIndex) {
    initFromTable(spwTable, bandIndex);
  }

  /**
   * Construct a new instance from a part of another band.
   * @param source Instance that is partially copied.
   * @param startChannel Start of range of channels that are copied.
   * @param endChannel End of range, exclusive.
   */
  BandData(const BandData& source, size_t startChannel, size_t endChannel)
      : _channelCount(endChannel - startChannel),
        _frequencyStep(source._frequencyStep),
        _referenceFrequency(source._referenceFrequency) {
    if (_channelCount == 0) throw std::runtime_error("No channels in set");
    if (endChannel < startChannel)
      throw std::runtime_error("Invalid band specification");
    _channelFrequencies.resize(_channelCount);

    for (size_t index = 0; index != _channelCount; ++index) {
      _channelFrequencies[index] =
          source._channelFrequencies[index + startChannel];
    }
  }

  /**
   * Construct a banddata from an array with channel infos.
   */
  BandData(const std::vector<ChannelInfo>& channels, double referenceFrequency)
      : _referenceFrequency(referenceFrequency) {
    initFromArray(channels);
  }

  /** Iterator over frequencies, pointing to first channel */
  double* begin() { return _channelFrequencies.begin(); }
  /** Iterator over frequencies, pointing past last channel */
  double* end() { return _channelFrequencies.end(); }
  /** Constant iterator over frequencies, pointing to first channel */
  const double* begin() const { return _channelFrequencies.begin(); }
  /** Constant iterator over frequencies, pointing to last channel */
  const double* end() const { return _channelFrequencies.end(); }

  /** Reverse iterator over frequencies, pointing to last channel */
  std::reverse_iterator<double*> rbegin() {
    return std::reverse_iterator<double*>(end());
  }

  /** Reverse iterator over frequencies, pointing past first channel */
  std::reverse_iterator<double*> rend() {
    return std::reverse_iterator<double*>(begin());
  }

  /** Constant reverse iterator over frequencies, pointing to last channel */
  std::reverse_iterator<const double*> rbegin() const {
    return std::reverse_iterator<const double*>(end());
  }

  /** Constant reverse iterator over frequencies, pointing past first channel */
  std::reverse_iterator<const double*> rend() const {
    return std::reverse_iterator<const double*>(begin());
  }

  /**
   * Assign new frequencies to this instance. The reference frequency
   * remains unmodified.
   * @param channelCount Number of channels.
   * @param frequencies Array of @p channelCount doubles containing the channel
   * frequencies.
   */
  void Set(size_t channelCount, const double* frequencies) {
    _channelCount = channelCount;
    _channelFrequencies.assign(frequencies, frequencies + channelCount);
  }

  /** Retrieve number of channels in this band.
   * @returns Number of channels.
   */
  size_t ChannelCount() const { return _channelCount; }

  /** Get the frequency in Hz of a specified channel.
   * @param channelIndex Zero-indexed channel index.
   */
  double ChannelFrequency(size_t channelIndex) const {
    return _channelFrequencies[channelIndex];
  }

  /** Get the channelwidth in Hz of a specified channel.
   * @param channelIndex Zero-indexed channel index.
   */
  double ChannelWidth(size_t /*channelIndex*/) const { return _frequencyStep; }

  /** Get information of a specified channel.
   * @param channelIndex Zero-indexed channel index.
   */
  ChannelInfo Channel(size_t channelIndex) const {
    return ChannelInfo(_channelFrequencies[channelIndex], _frequencyStep);
  }

  /** Get the wavelength in m of a specified channel.
   * @param channelIndex Zero-indexed channel index.
   */
  double ChannelWavelength(size_t channelIndex) const {
    return c() / _channelFrequencies[channelIndex];
  }

  /**
   * Get the frequency of the last channel.
   * In case the frequencies are stored in reverse channel order, the frequency
   * of the first channel is returned.
   * @returns Highest frequency.
   */
  double HighestFrequency() const {
    return _channelCount == 0               ? 0
           : lastChannel() > firstChannel() ? lastChannel()
                                            : firstChannel();
  }

  /**
   * Get the frequency of the first channel.
   * In case the frequencies are stored in reverse channel order, the frequency
   * of the last channel is returned.
   * @returns Lowest frequency.
   */
  double LowestFrequency() const {
    return _channelCount == 0
               ? 0
               : (firstChannel() < lastChannel() ? firstChannel()
                                                 : lastChannel());
  }

  /** Get the centre frequency.
   * @returns 0.5 * (HighestFrequency + LowestFrequency)
   */
  double CentreFrequency() const {
    return (HighestFrequency() + LowestFrequency()) * 0.5;
  }

  /**
   * @brief Get the reference frequency in Hz as stored in the spectral window
   * table. Can be slightly different from centre frequency.
   */
  double ReferenceFrequency() const { return _referenceFrequency; }

  /** Convert a frequency to a wavelength.
   * @param frequencyHz Frequency in Hz.
   * @returns Wavelength in m.
   */
  static double FrequencyToLambda(double frequencyHz) {
    return c() / frequencyHz;
  }

  /** Get the wavelength of the central channel.
   * @returns Central channel wavelength.
   */
  double CentreWavelength() const {
    return c() / ((HighestFrequency() + LowestFrequency()) * 0.5);
  }

  /** Get the distance between channels in Hz.
   * @returns Distance between channels.
   */
  double FrequencyStep() const { return _frequencyStep; }

  /** Get the wavelength of the first channel.
   * @returns longest wavelength. */
  double LongestWavelength() const {
    return _channelCount == 0 ? 0 : c() / LowestFrequency();
  }

  /**
   * Get the wavelength of the last channel.
   * @returns smallest wavelength.
   */
  double SmallestWavelength() const {
    return _channelCount == 0 ? 0 : c() / HighestFrequency();
  }

  /** Get the start of the frequency range covered by this band.
   * @returns Start of the band in Hz.
   */
  double BandStart() const { return LowestFrequency() - FrequencyStep() * 0.5; }
  /** Get the end of the frequency range covered by this band.
   * @returns End of the band in Hz. */
  double BandEnd() const { return HighestFrequency() + FrequencyStep() * 0.5; }

  /** Get the total bandwidth covered by this band.
   * @returns Bandwidth in Hz. */
  double Bandwidth() const {
    return HighestFrequency() - LowestFrequency() + FrequencyStep();
  }

 private:
  void initFromTable(const casacore::MSSpectralWindow& spwTable,
                     size_t bandIndex) {
    casacore::ScalarColumn<int> numChanCol(
        spwTable, casacore::MSSpectralWindow::columnName(
                      casacore::MSSpectralWindowEnums::NUM_CHAN));
    int temp;
    numChanCol.get(bandIndex, temp);
    _channelCount = temp;
    if (_channelCount == 0) throw std::runtime_error("No channels in set");

    casacore::ArrayColumn<double> chanFreqCol(
        spwTable, casacore::MSSpectralWindow::columnName(
                      casacore::MSSpectralWindowEnums::CHAN_FREQ));
    casacore::ArrayColumn<double> chanWidthCol(
        spwTable, casacore::MSSpectralWindow::columnName(
                      casacore::MSSpectralWindowEnums::CHAN_WIDTH));
    casacore::Array<double> channelFrequencies, channelWidths;
    chanFreqCol.get(bandIndex, channelFrequencies, true);
    chanWidthCol.get(bandIndex, channelWidths, true);

    _channelFrequencies.resize(_channelCount);
    size_t index = 0;
    for (casacore::Array<double>::const_iterator i = channelFrequencies.begin();
         i != channelFrequencies.end(); ++i) {
      _channelFrequencies[index] = *i;
      ++index;
    }
    _frequencyStep = 0.0;
    index = 0;
    for (casacore::Array<double>::const_iterator i = channelWidths.begin();
         i != channelWidths.end(); ++i) {
      _frequencyStep += *i;
      ++index;
    }
    _frequencyStep /= double(index);

    casacore::ScalarColumn<double> referenceFrequencyColumn(
        spwTable, casacore::MSSpectralWindow::columnName(
                      casacore::MSSpectralWindowEnums::REF_FREQUENCY));
    _referenceFrequency = referenceFrequencyColumn(bandIndex);
  }

  void initFromArray(const std::vector<ChannelInfo>& channels) {
    _channelCount = channels.size();
    _channelFrequencies.resize(_channelCount);
    size_t index = 0;
    _frequencyStep = 0.0;
    for (const ChannelInfo& channel : channels) {
      _channelFrequencies[index] = channel.Frequency();
      _frequencyStep += channel.Width();
      ++index;
    }
    _frequencyStep /= double(index);
  }

  double firstChannel() const { return _channelFrequencies[0]; }
  double lastChannel() const { return _channelFrequencies[_channelCount - 1]; }

  size_t _channelCount;
  aocommon::UVector<double> _channelFrequencies;
  double _frequencyStep;
  double _referenceFrequency;
};

}  // namespace aocommon

#endif
