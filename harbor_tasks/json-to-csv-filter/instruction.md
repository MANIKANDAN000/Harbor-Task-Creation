# JSON to CSV Filter Task

## Objective
Your task is to process a JSON data file located at `/app/input.json`. 

## Requirements
1.  Read the JSON array of users from `/app/input.json`.
2.  Filter the users to include **only** those who have `"active": true`.
3.  For each active user, extract their `name` and `email`.
4.  Write the results to a CSV file at `/app/output.csv`.
5.  The CSV file must have a header: `name,email`.

## File Paths
- **Input:** `/app/input.json`
- **Output:** `/app/output.csv`

## Example Data
Input:
```json
[
  {"name": "Alice", "email": "alice@example.com", "active": true},
  {"name": "Bob", "email": "bob@example.com", "active": false}
]
```

Expected Output (`/app/output.csv`):
```csv
name,email
Alice,alice@example.com
```
