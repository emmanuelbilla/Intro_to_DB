-- Display the full description of the 'books'

SELECT 
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Nullable',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default Value',
    EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = alx_book_store()
  AND TABLE_NAME = 'books';