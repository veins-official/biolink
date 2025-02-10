#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "matrix_functions.h"


int normalize (double *matrix, int rows, int cols, double c)
{
	double sum;
	int i, j;

	for (j = 0; j < cols; j++)
	{
		for (i = 0, sum = 0; i < rows; i++) sum += matrix[i * cols + j];
		for (i = 0; i < rows; i++) matrix[i * cols + j] = log (c * matrix[i * cols + j] / sum + 1);
	}

	return 0;
}

double calculate_mean (double *matrix, int cols, int row)
{
	double sum;
	int j;
	
	for (j = 0, sum = 0; j < cols; j++) sum += matrix[row * cols + j];
	return sum / cols;
}

double calculate_variance (double *matrix, int cols, int row, double mean)
{
	double diff, variance = 0;
	int j;
	
	for (j = 0; j < cols; j++)
	{
		diff = matrix[row * cols + j] - mean;
		variance += diff * diff;
	}
	
	return variance / (cols - 1);
}

int clear_matrix (double *matrix, int rows, int cols, double min_mean, double max_mean, double min_variance)
{
	double mean, variance;
	int i, j;
    
	for (i = 0; i < rows; i++)
	{
		mean = calculate_mean (matrix, cols, i);
		variance = calculate_variance (matrix, cols, i, mean);
		
		if ((mean < min_mean || mean > max_mean) || variance < min_variance) // "and" or "or"
		{
			for (j = 0; j < cols; j++) matrix[i * cols + j] = matrix[(rows - 1) * cols + j];
			i--; rows--;
		}
	}
	
	return rows;
}

int remove_dependence (double *matrix, int rows, int cols, int new_rows)
{
	double *variances;
	double mean, tmp;
	int i, j, k, max;
	
	if (new_rows >= rows) return rows;
	
	variances = (double*) malloc (rows * sizeof (double));
	for (i = 0; i < rows; i++)
	{
		mean = calculate_mean (matrix, cols, i);
		variances[i] = calculate_variance (matrix, cols, i, mean);
	}
	
	for (i = 0; i < new_rows; i++)
	{
		max = i;
		for (j = i + 1; j < rows; j++)
		{
			if (variances[j] > variances[max]) max = j;
		}
		
		for (k = 0; k < cols; k++)
		{
			tmp = matrix[max * cols + k];
			matrix[max * cols + k] = matrix[i * cols + k];
			matrix[i * cols + k] = tmp;
		}
	}
	
	return new_rows;
}

