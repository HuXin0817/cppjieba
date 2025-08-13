#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <utility>
#include <vector>

#include "cppjieba/Jieba.hpp"
#include "cppjieba/KeywordExtractor.hpp"

using namespace cppjieba;
using namespace std;

namespace py = pybind11;

PYBIND11_MODULE(cppjieba, m) {
  // Word structure binding
  py::class_<KeywordExtractor::Word>(m, "Word")
      .def_readonly("word", &KeywordExtractor::Word::word)
      .def_readonly("offsets", &KeywordExtractor::Word::offsets)
      .def_readonly("weight", &KeywordExtractor::Word::weight);

  // Jieba class binding
  py::class_<Jieba>(m, "Jieba")
      // Constructor
      .def(py::init<const string &, const string &, const string &,
                    const string &, const string &>(),
           py::arg("dict_path") = "", py::arg("model_path") = "",
           py::arg("user_dict_path") = "", py::arg("idf_path") = "",
           py::arg("stop_word_path") = "")

      // Cut methods
      .def(
          "Cut",
          [](const Jieba &self, const string &sentence, bool hmm) {
            vector<string> words;
            self.Cut(sentence, words, hmm);
            return words;
          },
          py::arg("sentence"), py::arg("hmm") = true)

      .def(
          "CutAll",
          [](const Jieba &self, const string &sentence) {
            vector<string> words;
            self.CutAll(sentence, words);
            return words;
          },
          py::arg("sentence"))

      .def(
          "CutForSearch",
          [](const Jieba &self, const string &sentence, bool hmm) {
            vector<string> words;
            self.CutForSearch(sentence, words, hmm);
            return words;
          },
          py::arg("sentence"), py::arg("hmm") = true)

      .def(
          "CutHMM",
          [](const Jieba &self, const string &sentence) {
            vector<string> words;
            self.CutHMM(sentence, words);
            return words;
          },
          py::arg("sentence"))

      .def(
          "CutSmall",
          [](const Jieba &self, const string &sentence, size_t max_word_len) {
            vector<string> words;
            self.CutSmall(sentence, words, max_word_len);
            return words;
          },
          py::arg("sentence"), py::arg("max_word_len"))

      // Tagging
      .def(
          "Tag",
          [](const Jieba &self, const string &sentence) {
            vector<pair<string, string>> tags;
            self.Tag(sentence, tags);
            return tags;
          },
          py::arg("sentence"))

      .def("LookupTag", &Jieba::LookupTag, py::arg("str"))

      // User dictionary - simplified to avoid overloading issues
      .def(
          "InsertUserWord",
          [](Jieba &self, const string &word, const string &tag) {
            return self.InsertUserWord(word, tag);
          },
          py::arg("word"), py::arg("tag") = "n")

      .def(
          "InsertUserWordWithFreq",
          [](Jieba &self, const string &word, int freq, const string &tag) {
            return self.InsertUserWord(word, freq, tag);
          },
          py::arg("word"), py::arg("freq"), py::arg("tag") = "n")

      .def(
          "DeleteUserWord",
          [](Jieba &self, const string &word, const string &tag) {
            return self.DeleteUserWord(word, tag);
          },
          py::arg("word"), py::arg("tag") = "n")

      .def(
          "Find",
          [](Jieba &self, const string &word) { return self.Find(word); },
          py::arg("word"))

      .def(
          "ResetSeparators",
          [](Jieba &self, const string &s) { self.ResetSeparators(s); },
          py::arg("s"))

      .def(
          "LoadUserDict",
          [](Jieba &self, const string &path) { self.LoadUserDict(path); },
          py::arg("path"))

      // Keyword Extractor
      .def_readonly("extractor", &Jieba::extractor);

  // KeywordExtractor class binding
  py::class_<KeywordExtractor>(m, "KeywordExtractor")
      .def(
          "extract",
          [](KeywordExtractor &self, const string &sentence, int topK,
             bool withWeight) -> py::object {
            if (withWeight) {
              vector<pair<string, double>> keywords;
              self.Extract(sentence, keywords, topK);
              return py::cast(keywords);
            } else {
              vector<string> keywords;
              self.Extract(sentence, keywords, topK);
              return py::cast(keywords);
            }
          },
          py::arg("sentence"), py::arg("topK") = 20,
          py::arg("withWeight") = false)

      .def(
          "extract_with_offsets",
          [](KeywordExtractor &self, const string &sentence, int topK) {
            vector<KeywordExtractor::Word> keywords;
            self.Extract(sentence, keywords, topK);
            return keywords;
          },
          py::arg("sentence"), py::arg("topK") = 20);
}
