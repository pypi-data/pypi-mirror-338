/*
 * Copyright (C) 2023 Simon Stahlberg
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

#ifndef SRC_GRAPHS_ALGORITHMS_NAUTY_SPARSE_IMPL_HPP_
#define SRC_GRAPHS_ALGORITHMS_NAUTY_SPARSE_IMPL_HPP_

// Only include nauty_sparse_impl.hpp in a source file to avoid transitive includes of nauty.h.
#include "mimir/graphs/algorithms/nauty.hpp"
#include "mimir/graphs/declarations.hpp"

#include <nausparse.h>
#include <nauty.h>
#include <sstream>
#include <string>
#include <vector>

namespace mimir::graphs::nauty
{

class SparseGraphImpl
{
private:
    // num_vertices
    size_t n_;
    // vertex capacity
    size_t c_;
    // Track existing edges to avoid duplicates
    std::vector<bool> adj_matrix_;

    // The input graph
    sparsegraph graph_;
    bool use_default_ptn_;

    mimir::graphs::ColorList canon_coloring_;
    std::vector<int> lab_;
    std::vector<int> ptn_;

    // The canonical graph
    sparsegraph canon_graph_;

    // Output streams
    std::stringstream canon_graph_repr_;
    std::stringstream canon_graph_compressed_repr_;

    void copy_graph_data(const sparsegraph& in_graph, sparsegraph& out_graph) const;

    void initialize_graph_data(sparsegraph& out_graph) const;

    void allocate_graph(sparsegraph& out_graph) const;
    void deallocate_graph(sparsegraph& the_graph) const;

public:
    explicit SparseGraphImpl(size_t num_vertices);
    SparseGraphImpl(const SparseGraphImpl& other);
    SparseGraphImpl& operator=(const SparseGraphImpl& other);
    SparseGraphImpl(SparseGraphImpl&& other) noexcept;
    SparseGraphImpl& operator=(SparseGraphImpl&& other) noexcept;
    ~SparseGraphImpl();

    void add_edge(size_t source, size_t target);

    void add_vertex_coloring(const mimir::graphs::ColorList& vertex_coloring);

    Certificate compute_certificate();

    void clear(size_t num_vertices);

    bool is_directed() const;
    bool has_loop() const;
};

extern std::ostream& operator<<(std::ostream& out, const sparsegraph& graph);

}

#endif
