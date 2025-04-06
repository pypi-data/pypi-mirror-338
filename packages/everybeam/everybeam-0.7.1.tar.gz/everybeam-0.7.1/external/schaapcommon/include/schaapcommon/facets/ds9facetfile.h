// Copyright (C) 2020 ASTRON (Netherlands Institute for Radio Astronomy)
// SPDX-License-Identifier: GPL-3.0-or-later

#ifndef SCHAAPCOMMON_FACETS_DS9FACETFILE_H_
#define SCHAAPCOMMON_FACETS_DS9FACETFILE_H_

#include "facet.h"

#include <cmath>
#include <fstream>
#include <memory>
#include <vector>

namespace schaapcommon {
namespace facets {

/**
 * Class for reading facets from a DS9 region file.
 *
 * Facets are specified using "polygons", where the (ra,dec)
 * coordinates of the polygon vertices are specified sequentially, i.e.
 *
 * \code{.unparsed}
 * polygon(ra_0, dec_0, ..., ..., ra_n, dec_n)
 * \endcode
 *
 * Note that the (ra,dec) coordinates should be given in degrees!
 *
 * In addition, each polygon can be equipped with text labels and/or a specific
 * point of interest. The text label should be specified on the same line as the
 * \c polygon to which it should be attached and should be preceded by a \c #,
 * e.g.:
 *
 * \code{.unparsed}
 * polygon(ra_0, dec_0, ..., ..., ra_n, dec_n) # text="ABCD"
 * \endcode
 *
 * A \c point can be attached to a polygon to mark a specific point of interest.
 * Similar to the polygon definition, the coordinates are provided in (ra,dec)
 * in degrees. A point should be placed on a new line, following the polygon
 * definition, i.e.:
 *
 * \code{.unparsed}
 * polygon(ra_0, dec_0, ..., ..., ra_n, dec_n) # text="ABCD"
 * point(ra_A,dec_A)
 * \endcode
 *
 * Only one point can be attached per polygon. In case multiple points were
 * specified, the last one will be used. So in the following example:
 *
 * \code{.unparsed}
 * polygon(ra_0, dec_0, ..., ..., ra_n, dec_n) # text="ABCD"
 * point(ra_A,dec_A)
 * point(ra_B,dec_B)
 * \endcode
 * the \c point(ra_A,dec_A) is ignored and \c point(ra_B,dec_B) will be used.
 */
class DS9FacetFile {
 public:
  enum class TokenType { kEmpty, kWord, kNumber, kSymbol, kComment };

  /**
   * @brief Construct a new DS9FacetFile object
   *
   * @param filename path to DS9 region file
   */
  explicit DS9FacetFile(const std::string& filename)
      : file_(filename),
        token_(""),
        type_(TokenType::kEmpty),
        has_char_(false),
        char_() {
    if (!file_) {
      throw std::runtime_error("Error reading " + filename);
    }
    Skip();
  }

  /**
   * Read the facets from the file. Be aware that this does not
   * set the pixel values (x, y) of the vertices, see
   * @ref Facet::CalculatePixelPositions().
   */
  std::vector<Facet> Read(const Facet::InitializationData& data) {
    std::vector<Facet> facets;
    std::vector<Coord> coordinates;
    std::string direction_label;
    std::optional<Coord> direction;
    while (Type() != TokenType::kEmpty) {
      std::string t = Token();
      if (t == "global" || t == "fk5") {
        SkipLine();
      } else if (Type() == TokenType::kComment) {
        Skip();
      } else if (Type() == TokenType::kWord) {
        Skip();

        if (t == "polygon") {
          if (!coordinates.empty()) {
            facets.emplace_back(data, std::move(coordinates),
                                std::move(direction));
            facets.back().SetDirectionLabel(direction_label);
            direction.reset();
          }
          coordinates = ReadPolygon();
          direction_label = ParseDirectionLabel(Type(), Token());
        } else if (t == "point" && !coordinates.empty()) {
          direction = ReadPoint();
          const std::string direction_label_point =
              ParseDirectionLabel(Type(), Token());
          if (direction_label_point != "") {
            direction_label = direction_label_point;
          }
        }
      }
    }

    if (!coordinates.empty()) {
      facets.emplace_back(data, std::move(coordinates), std::move(direction));
      facets.back().SetDirectionLabel(direction_label);
    }

    return facets;
  }

  std::vector<std::shared_ptr<Facet>> ReadShared(
      const Facet::InitializationData& data) {
    std::vector<std::shared_ptr<Facet>> facets;
    std::vector<Coord> coordinates;
    std::string direction_label;
    std::optional<Coord> direction;
    while (Type() != TokenType::kEmpty) {
      std::string t = Token();
      if (t == "global" || t == "fk5") {
        SkipLine();
      } else if (Type() == TokenType::kComment) {
        Skip();
      } else if (Type() == TokenType::kWord) {
        Skip();

        if (t == "polygon") {
          if (!coordinates.empty()) {
            facets.push_back(std::make_shared<Facet>(
                data, std::move(coordinates), std::move(direction)));
            facets.back()->SetDirectionLabel(direction_label);
            direction.reset();
          }
          coordinates = ReadPolygon();
          direction_label = ParseDirectionLabel(Type(), Token());
        } else if (t == "point" && !coordinates.empty()) {
          direction = ReadPoint();
        }
      }
    }

    if (!coordinates.empty()) {
      facets.push_back(std::make_shared<Facet>(data, std::move(coordinates),
                                               std::move(direction)));
      facets.back()->SetDirectionLabel(direction_label);
    }

    return facets;
  }

  /**
   * Count the number of facets in the file.
   * @return The number of facets in the file.
   */
  size_t Count() {
    size_t count = 0;
    while (Type() != TokenType::kEmpty) {
      std::string t = Token();
      if (t == "global" || t == "fk5") {
        SkipLine();
      } else if (Type() == TokenType::kComment) {
        Skip();
      } else if (Type() == TokenType::kWord) {
        Skip();
        if (t == "polygon") {
          ReadPolygon();
          ++count;
        } else if (t == "point") {
          ReadPoint();
        }
      }
    }

    return count;
  }

  /**
   * Take a comment as input e.g. text={direction} and retrieves direction.
   */
  static std::string ParseDirectionLabel(TokenType type,
                                         const std::string& comment) {
    const std::string classifier = "text=";
    std::string dir = "";

    if (type == TokenType::kComment &&
        comment.find(classifier) != std::string::npos) {
      dir = comment.substr(comment.find(classifier) + classifier.length(),
                           comment.length());
      // Remove trailing parts
      dir = dir.substr(0, dir.find(","))
                .substr(0, dir.find(" "))
                .substr(0, dir.find("\n"));
    }

    return dir;
  }

 private:
  std::vector<Coord> ReadPolygon() {
    const std::vector<double> vals = ReadNumList();
    if (vals.size() % 2 != 0) {
      throw std::runtime_error(
          "Polygon is expecting an even number of numbers in its list");
    }
    std::vector<Coord> coordinates;
    coordinates.reserve(vals.size() / 2);
    auto i = vals.cbegin();
    while (i != vals.cend()) {
      const double ra = *i * (M_PI / 180.0);
      ++i;
      const double dec = *i * (M_PI / 180.0);
      ++i;
      coordinates.emplace_back(ra, dec);
    }

    return coordinates;
  }

  Coord ReadPoint() {
    const std::vector<double> vals = ReadNumList();
    if (vals.size() != 2) {
      throw std::runtime_error(
          "Point is expecting exactly two numbers in its list");
    }
    const double ra = vals[0] * (M_PI / 180.0);
    const double dec = vals[1] * (M_PI / 180.0);
    return Coord(ra, dec);
  }

  std::vector<double> ReadNumList() {
    std::vector<double> vals;
    if (Token() != "(") {
      throw std::runtime_error("Expecting '(' after polygon keyword");
    }
    Skip();
    while (Token() != ")") {
      if (Type() != TokenType::kNumber) {
        throw std::runtime_error("Expected number or ')' after '(' ");
      }
      vals.push_back(atof(Token().c_str()));
      Skip();
      if (Token() == ",") Skip();
    }
    Skip();
    return vals;
  }

  std::string Token() const { return token_; }

  TokenType Type() const { return type_; }

  void SkipLine() {
    char c;
    while (NextChar(c)) {
      if (c == '\n') break;
    }
    Skip();
  }

  void Skip() {
    bool cont = true;
    type_ = TokenType::kEmpty;
    token_ = std::string();
    do {
      char c;
      if (NextChar(c)) {
        switch (type_) {
          case TokenType::kEmpty:
            if (IsAlpha(c)) {
              type_ = TokenType::kWord;
              token_ += c;
            } else if (IsWhiteSpace(c)) {
            } else if (IsNumeric(c)) {
              type_ = TokenType::kNumber;
              token_ += c;
            } else if (c == '(' || c == ')' || c == ',') {
              type_ = TokenType::kSymbol;
              token_ += c;
              cont = false;
            } else if (c == '#') {
              type_ = TokenType::kComment;
            }
            break;
          case TokenType::kWord:
            if (IsAlpha(c) || (c >= '0' && c <= '9')) {
              token_ += c;
            } else {
              cont = false;
              PushChar(c);
            }
            break;
          case TokenType::kNumber:
            if (IsNumeric(c)) {
              token_ += c;
            } else {
              cont = false;
              PushChar(c);
            }
            break;
          case TokenType::kSymbol:
            PushChar(c);
            cont = false;
            break;
          case TokenType::kComment:
            if (c == '\n') {
              cont = false;
            } else {
              token_ += c;
            }
            break;
        }
      } else {
        cont = false;
      }
    } while (cont);
  }

  bool NextChar(char& c) {
    if (has_char_) {
      has_char_ = false;
      c = char_;
      return true;
    } else {
      file_.read(&c, 1);
      return file_.good();
    }
  }
  void PushChar(char c) {
    has_char_ = true;
    char_ = c;
  }

  std::ifstream file_;
  std::string token_;
  TokenType type_;
  bool has_char_;
  char char_;

  constexpr static bool IsAlpha(char c) {
    return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || c == '_';
  }
  constexpr static bool IsWhiteSpace(char c) {
    return c == ' ' || c == '\n' || c == '\r' || c == '\t';
  }
  constexpr static bool IsNumeric(char c) {
    return (c >= '0' && c <= '9') || c == '-' || c == '.';
  }
};
}  // namespace facets
}  // namespace schaapcommon

#endif  // SCHAAPCOMMON_FACETS_DS9FACETFILE_H_
