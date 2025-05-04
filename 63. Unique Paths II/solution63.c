#include <stdbool.h>
#include <stdlib.h>
#include <assert.h>

#include <stdbool.h>
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

int uniquePathsWithObstacles(int **grid, int ROWS, int *COLS)
{
    grid[0][0] = (grid[0][0] << 1) + !grid[0][0];
    for (size_t col = 1; col < *COLS; ++col)
    {
        if (grid[0][col] == 1)
            grid[0][0] |= 4;
        grid[0][col] = grid[0][col] == 0 && !(grid[0][0] & 6) ? 1 : 0;
    }
    for (size_t row = 1; row < ROWS; ++row)
    {
        if (grid[row][0] == 1)
            grid[0][0] |= 8;
        grid[row][0] = grid[row][0] == 0 && !(grid[0][0] & 10) ? 1 : 0;
    }
    grid[0][0] &= 1;


    for (size_t row = 1; row < ROWS; ++row)
    {
        for (size_t col = 1; col < *COLS; ++col)
        {
            grid[row][col] = grid[row][col] == 0 ? grid[row - 1][col] + grid[row][col - 1] : 0;
        }
    }
    return grid[ROWS - 1][*COLS - 1];
}

int main()
{
    int ROWS = 2, COLS = 1;
    int **grid = (int **)malloc(sizeof(int *) * ROWS);
    for (size_t row = 0; row < ROWS; ++row)
    {
        grid[row] = malloc(sizeof(int) * COLS);
    }
    grid[0][0] = 1;
    grid[1][0] = 0;
    int ans = uniquePathsWithObstacles(grid, ROWS, &COLS);
    printf("ans == %d\n", ans);
    assert(ans == 0);
    for (size_t row = 0; row < ROWS; ++row)
    {
        free(grid[row]);
    }
    free(grid);

    return 0;
}