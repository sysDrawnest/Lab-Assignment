# Assignment-4 Solutions (NumPy + Pandas)

import numpy as np
import pandas as pd

print("----- NumPy Section -----")

# 1. Create a 1D array from a list.
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array from list:", arr1)

# 2. Create a 3x3 array of zeros.
zeros_arr = np.zeros((3, 3))
print("\n3x3 array of zeros:\n", zeros_arr)

# 3. Create a 2x2 array of ones.
ones_arr = np.ones((2, 2))
print("\n2x2 array of ones:\n", ones_arr)

# 4. Generate array from 0 to 10 (exclusive).
range_arr = np.arange(0, 10)
print("\nArray from 0 to 10 (exclusive):", range_arr)

# 5. Create 5 evenly spaced numbers between 0 and 1.
linspace_arr = np.linspace(0, 1, 5)
print("\n5 evenly spaced numbers between 0 and 1:", linspace_arr)

# 6. Create a 4x4 identity matrix.
identity_mat = np.eye(4)
print("\n4x4 identity matrix:\n", identity_mat)

# 7. Reshape 1D array to 2D.
arr2 = np.arange(6)
reshaped_arr = arr2.reshape(2, 3)
print("\nReshaped 1D array to 2D:\n", reshaped_arr)

# 8. Get the shape and dtype of an array.
print("\nShape:", reshaped_arr.shape)
print("Dtype:", reshaped_arr.dtype)

# 9. Reverse a NumPy array.
reversed_arr = arr2[::-1]
print("\nReversed array:", reversed_arr)

# 10. Extract even numbers from an array.
even_numbers = arr2[arr2 % 2 == 0]
print("\nEven numbers:", even_numbers)

# 11. Find the max in each row.
arr3 = np.array([[1, 5, 3], [7, 2, 8]])
max_in_rows = np.max(arr3, axis=1)
print("\nMax in each row:", max_in_rows)

# 12. Compute the mean, std, and median of an array.
arr4 = np.array([1, 2, 3, 4, 5])
print("\nMean:", np.mean(arr4))
print("Std:", np.std(arr4))
print("Median:", np.median(arr4))

# 13. Stack two arrays vertically.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked_v = np.vstack((a, b))
print("\nStacked vertically:\n", stacked_v)

# 14. Stack two arrays horizontally.
stacked_h = np.hstack((a, b))
print("\nStacked horizontally:", stacked_h)

# 15. (Duplicate) Stack two arrays horizontally.
print("\nStacked horizontally (again):", stacked_h)

# 16. Find the unique values and their counts.
arr5 = np.array([1, 2, 2, 3, 3, 3])
unique, counts = np.unique(arr5, return_counts=True)
print("\nUnique values:", unique)
print("Counts:", counts)

# 17. Replace NaN with column means.
arr6 = np.array([[1, 2, np.nan], [4, np.nan, 6]])
col_means = np.nanmean(arr6, axis=0)
inds = np.where(np.isnan(arr6))
arr6[inds] = np.take(col_means, inds[1])
print("\nNaN replaced with column means:\n", arr6)

# 18. Get index of min and max values.
arr7 = np.array([3, 1, 5, 2])
print("\nIndex of min:", np.argmin(arr7))
print("Index of max:", np.argmax(arr7))

# 19. Create a 3D array of random integers.
arr8 = np.random.randint(0, 10, size=(2, 3, 4))
print("\n3D array of random integers:\n", arr8)

# 20. Use np.where() to replace values.
arr9 = np.array([1, 2, 3, 4, 5])
replaced_arr = np.where(arr9 > 3, 0, arr9)
print("\nValues >3 replaced with 0:", replaced_arr)

print("\n----- Pandas Section -----")

# 1. Create a Series using a Python list.
series1 = pd.Series([10, 20, 30])
print("\nSeries from list:\n", series1)

# 2. Create a Series with custom string indices.
series2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print("\nSeries with custom indices:\n", series2)

# 3. Create a Series from a dictionary.
data = {'x': 10, 'y': 20, 'z': 30}
series3 = pd.Series(data)
print("\nSeries from dictionary:\n", series3)

# 4. Access first 3 elements of a Series.
print("\nFirst 3 elements of series1:\n", series1.head(3))

# 5. Filter Series elements greater than 50.
filtered = series3[series3 > 15]
print("\nFiltered Series (values >15):\n", filtered)

# 6. Add two Series with different indices.
series4 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series5 = pd.Series([4, 5], index=['b', 'c'])
sum_series = series4.add(series5, fill_value=0)
print("\nSum of two Series:\n", sum_series)

# 7. Multiply a Series by a scalar.
print("\nSeries4 multiplied by 2:\n", series4 * 2)

# 8. Use .multiply() method to multiply with scalar.
print("\nSeries4 multiplied by 3 using .multiply():\n", series4.multiply(3))

# 10. Sort Series by values descending.
print("\nSeries4 sorted descending:\n", series4.sort_values(ascending=False))

# 11. Sort Series by index.
print("\nSeries4 sorted by index:\n", series4.sort_index())

# 12. Check for null values.
series6 = pd.Series([1, np.nan, 3])
print("\nCheck for null values:\n", series6.isnull())

# 14. Concatenate two Series using concat().
concat_series = pd.concat([series4, series5])
print("\nConcatenated Series:\n", concat_series)

# 15. Concatenate two Series using append().
append_series = series4.append(series5)
print("\nAppended Series:\n", append_series)

# 16. Retrieve first 5 elements using .head()
print("\nFirst 5 elements:\n", concat_series.head(5))

# 17. Retrieve last 5 elements using .tail()
print("\nLast 5 elements:\n", concat_series.tail(5))

# 18. Convert Series to DataFrame.
df = series4.to_frame(name='Values')
print("\nSeries4 as DataFrame:\n", df)

# 19. Replace NaN with 0.
print("\nSeries6 with NaN replaced with 0:\n", series6.fillna(0))

# 20. Drop missing values.
print("\nSeries6 without NaN:\n", series6.dropna())

# 21. Check Series data type.
print("\nData type of Series4:", series4.dtype)
