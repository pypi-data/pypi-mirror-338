#ifndef PAGINATE_H
#define PAGINATE_H

#include <stdbool.h>
#include "sqlite3.h"
#include "../include/vec_types.h"

typedef struct IdIndexPair
{
    int id;
    int index;
} IdIndexPair;

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif

    EXPORT PaginationResults *get_vectors_with_pagination(const char *file_path, const int skip, const int limit);
    int compare_id_index_pairs(const void *a, const void *b);
    bool get_metadata_batch_paginate(sqlite3 *db, PaginationItem *results, int batch_start, int batch_size);
    char *create_id_list(PaginationItem *items, int count);

#ifdef __cplusplus
}
#endif

#endif // PAGINATE_H