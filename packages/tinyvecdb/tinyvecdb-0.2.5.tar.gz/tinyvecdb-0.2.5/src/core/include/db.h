#ifndef DB_H
#define DB_H

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef _WIN32
#include <windows.h>
#define EXPORT __declspec(dllexport)
#else
#include <sys/time.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#define EXPORT __attribute__((visibility("default")))
#endif

#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include "file.h"
#include "vec_types.h"
#include "sqlite3.h"

    typedef struct TinyVecConnection
    {
        const char *file_path;
        uint32_t dimensions;
        FILE *vec_file;
        FILE *idx_file;
        FILE *md_file;
        MmapInfo *idx_mmap;
        MmapInfo *md_mmap;
        sqlite3 *sqlite_db;
    } TinyVecConnection;

    typedef struct
    {
        TinyVecConnection **connections;
        int active_connections;
    } ActiveTinyVecConnections;

    // Core API functions
    EXPORT TinyVecConnection *create_tiny_vec_connection(const char *file_path, const uint32_t dimensions);
    EXPORT IndexFileStats get_index_stats(const char *file_path);
    EXPORT DBSearchResult *get_top_k(const char *file_path, const float *query_vec, const int top_k);
    EXPORT DBSearchResult *get_top_k_with_filter(const char *file_path, const float *query_vec, const int top_k, const char *json_filter);
    EXPORT int delete_data_by_ids(const char *file_path, int *ids_to_delete, int delete_count);
    EXPORT int delete_data_by_filter(const char *file_path, const char *json_filter);
    EXPORT int insert_data(const char *file_path, float **vectors, char **metadatas, size_t *metadata_lengths,
                           const size_t vec_count, const uint32_t dimensions);
    EXPORT bool update_db_file_connection(const char *file_path);
    EXPORT int batch_update_items_by_id(const char *file_path, DBUpdateItem *items, int item_count);

    // Internal functions
    TinyVecConnection *get_tinyvec_connection(const char *file_path);
    bool add_to_connection_pool(TinyVecConnection *connection);
    size_t calculate_optimal_buffer_size(int dimensions);
    int get_metadata_batch(sqlite3 *db, VecResult *sorted, int count);
    bool get_filtered_ids(sqlite3 *db, const char *where_clause, int **ids_out, int *count_out);
    bool init_sqlite_table(sqlite3 *db);

#ifdef __cplusplus
}
#endif

// Platform-specific aligned memory functions
#ifdef _WIN32
#define aligned_malloc(size, alignment) _aligned_malloc(size, alignment)
#define aligned_free(ptr) _aligned_free(ptr)
#else
// For macOS and Linux
void *aligned_malloc(size_t size, size_t alignment);
#define aligned_free(ptr) free(ptr)
#endif

#endif // DB_H