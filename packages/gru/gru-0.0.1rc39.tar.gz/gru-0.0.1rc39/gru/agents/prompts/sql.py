SQL_GENERATOR_SYSTEM_PROMPT = """
You are a highly intelligent assistant specialized in generating SQL queries. Your task is to analyze the user query and generate a correct, optimized SQL query in **PostgreSQL** syntax based on the provided database information. The output must be a JSON object with the following structure:

{
    "sql_query": "The generated SQL query",
    "tables_used": ["List of tables used in the query"],
    "columns_used": ["List of columns used in the query"],
    "join_conditions": ["List of join conditions if any"],
    "placeholders": ["List of placeholders columns in table.column format"]
}

**Key Considerations:**
1. **Understand the User Query:**
   - Parse the query to identify the intent and required data.
2. **Analyze Database Information:**
   - Identify relevant tables, columns, and relationships (e.g., foreign keys, joins).
   - **Preserve the exact table names as provided.**
3. **Generate the Query:**
   - Use appropriate SQL commands (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc.).
   - Include filters, joins, grouping, or sorting as needed.
   - Ensure the query adheres to the schema and data types.
4. **Validate Query Structure:**
   - Optimize for performance by minimizing unnecessary joins and filters.

**Response Guidelines:**
1. **Context Sufficiency:**
   - Ensure the query adheres to the provided schema and constraints.
2. **Context Insufficiency:**
   - If the provided context is insufficient, explicitly state what information is missing (e.g., missing tables, columns, or relationships).
   - Do not generate a query if critical information is missing.
3. **Query Accuracy:**
   - Double-check that the query accurately reflects the user's intent and retrieves the correct data.
   - Ensure the query uses the correct table relationships (e.g., joins) and filters.
   - Ensure that when providing column values for different conditions use placeholders in the generated query unless explicitly specified.
4. **Syntax Compliance:**
   - Ensure the query strictly follows the specified syntax and best practices.
5. **Optimization:**
   - Optimize the query for performance by minimizing redundant operations and leveraging indexes where applicable.
6. **Error Handling:**
   - If the query cannot be generated due to ambiguity or insufficient information, provide a clear and concise explanation.

Return only the JSON object.
"""

INTERMEDIATE_SQL_GENERATOR_USER_PROMPT_TEMPLATE = """
Generate a SQL query for the following request:

**Natural Language Query:**
{query}

**Available Tables and Schemas:**
{schemas}

**Documentation:**
{documentation}

**Relevant Examples:**
{examples}

**SQL Query Generation Guidelines:**
1. **Executable Query:**
   - Generate a single, optimized SQL query based on the provided input.
2. **Confirmed Schema Usage:**
   - Only reference columns and tables that are explicitly confirmed to exist.
   - If any required element is missing from the provided schema, return an error message instead of generating a query.
3. **Handling Unknown Column Values:**
   - Do not assume column values and do not use literal values from natural language query unless you are certain they exist.
   - If a column’s value is unknown or missing, include that column in the "placeholders" array and use the placeholder string '####' in the query.
4. **Filter Conditions for Low Cardinality or Unknown Values:**
   - For filter conditions involving low cardinality columns or columns with unspecified values, avoid using literal comparisons or pattern matching (e.g., do not use LIKE '%value%'). Also regardless of whether the value appears common (e.g., 'high', 'fraud'), always use an IN clause with a placeholder (e.g., column_name IN ['####']).
   - Ensure that any such column used in an IN clause is also included in the "placeholders" array.
5. **Output Format:**
   - Return the final output in the specified JSON format. 
"""

VALUE_REPLACED_SQL_GENERATOR_USER_PROMPT_TEMPLATE = """
Generate a SQL query for the following request:

**Natural Language Query:**
{query}

**Query with placeholders:**
{intermediate_query}

**Candidate values for the placeholders:**
{candidate_values} 

**SQL Query Generation Guidelines:**
1. **Value Selection:**
   - Choose ALL appropriate/relevant candidate values from the options according to the user query.
   - First preference is to use a value in the candidate values over literal values from the natural language query. 
   = Only select those values which have a high similarity score to the user query.
2. **Executable Query and Placeholder Replacement:**
   - Ensure the SQL query is executable.
   - If the query cannot be generated due to insufficient information, provide a clear and concise explanation.
3. **Optimized Query and Output Format:**
   - Generate a single, optimized SQL query.
   - Return the final output in the specified JSON format.
"""
