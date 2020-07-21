NOTES

Topic -> PAGINATION at the Database Level

Requirement -> "Display" only i users data at a time -> WRONG KEY PHRASE

Requirement -> Display "only i users" data at a time -> CORRECT KEY PHRASE


General (WRONG) Approach

1 Million Users - 1,000,000
DB -> Limit, Offset -> NOT USED
Objective -> Retrieve i = 10 rows at a time

On the DB, your application executes the following query
    Select * from users;
        -> 1,000,000 rows
            -> in your main memory -> RAM
                -> Your Application will become less performant.
                -> Start crashing
                -> Other memory issues


2. In your application logic, you will 
    1. cut i rows 
    2. cut i rows 
    .
    .
    .
    .



Optimised (Correct) Approach

1 Million Users - 1,000,000
DB -> Limit, Offset
Objective -> Retrieve i = 10 rows at a time

Select Only i rows at a time
    -> Select * from users Limit 0 offset i
    -> Select * from users Limit i offset 2 * i
    .
    .
    .
    .
    .

Benefits
1. All the data is NOT loaded into the main memory
2. Responsibility of Pagination delegated to Model -> DB






___________________________________________________________-


Topic -- Object returned for Pagination

    items
    has_prev -> False when you are on the first page
    has_next -> False when you are on the last page
    next_num -> return the number of the next page
    prev_num -> return the number of the prev page
