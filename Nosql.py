import streamlit as st
import random
import base64

# Define your questions and answers

questions = [
    {
        "question": "Which data model is best suited for scenarios where related data is frequently accessed together and requires faster reads?",
        "options": ["Normalized data model", "Embedded data model", "Relational data model", "Graph data model"],
        "correct_answer": "Embedded data model"
    },
    {
        "question": "What is the primary advantage of using a normalized data model in MongoDB?",
        "options": ["Faster read operations", "Reduced data redundancy", "Simpler update operations", "Improved query flexibility"],
        "correct_answer": "Reduced data redundancy"
    },
    {
        "question": "Which MongoDB operation is used to insert a single document into a collection?",
        "options": ["insert()", "insertOne()", "insertDocument()", "addDocument()"],
        "correct_answer": "insertOne()"
    },
    {
        "question": "What is the return type of the `insertOne()` method in MongoDB?",
        "options": ["A boolean indicating success or failure", "The inserted document itself", "An object containing the `acknowledged` flag and `insertedId`", "An integer representing the number of documents inserted"],
        "correct_answer": "An object containing the `acknowledged` flag and `insertedId`"
    },
    {
        "question": "Which MongoDB operation is used to retrieve documents from a collection?",
        "options": ["get()", "find()", "select()", "query()"],
        "correct_answer": "find()"
    },
    {
        "question": "Which of the following query operators is used to match values greater than or equal to a specified value?",
        "options": ["$gt", "$lt", "$gte", "$lte"],
        "correct_answer": "$gte"
    },
    {
        "question": "Which projection operator is used to exclude a specific field from the result?",
        "options": ["include: 0", "exclude: 1", "field: false", "field: 0"],
        "correct_answer": "field: 0"
    },
    {
        "question": "What is the purpose of cursor methods in MongoDB?",
        "options": ["To modify documents directly", "To control the behavior of query results (e.g., sorting, limiting)", "To define indexes on collections", "To manage database connections"],
        "correct_answer": "To control the behavior of query results (e.g., sorting, limiting)"
    },
    {
        "question": "Which cursor method is used to sort the results of a query in ascending order?",
        "options": ["sort(field: 1)", "sort({field: 'asc'})", "orderBy(field)", "order(field)"],
        "correct_answer": "sort(field: 1)"
    },
    {
        "question": "Which cursor method is used to limit the number of documents returned by a query?",
        "options": ["restrict()", "limit()", "maxResults()", "truncate()"],
        "correct_answer": "limit()"
    },
    {
        "question": "Which operation replace only a single documents",
        "options": ["replaceOne()", "replaceMany()", "update()", "replace()"],
        "correct_answer": "replaceOne()"
    },
    {
        "question": "What is the purpose of the MongoDB aggregation framework?",
        "options": ["To define indexes on collections", "To perform complex data transformations and analysis", "To manage database connections", "To define user roles and permissions"],
        "correct_answer": "To perform complex data transformations and analysis"
    },
    {
        "question": "What is an aggregation pipeline in MongoDB?",
        "options": ["A sequence of stages that process documents", "A set of indexes that optimize query performance", "A collection of stored procedures", "A series of database backups"],
        "correct_answer": "A sequence of stages that process documents"
    },
    {
        "question": "Which aggregation pipeline stage is used to filter documents based on a specified condition?",
        "options": ["$filter", "$match", "$where", "$condition"],
        "correct_answer": "$match"
    },
    {
        "question": "Which aggregation pipeline stage is used to group documents based on a specified key?",
        "options": ["$cluster", "$group", "$bucket", "$aggregate"],
        "correct_answer": "$group"
    },
    {
        "question": "Which aggregation pipeline stage is used to reshape documents by adding, removing, or renaming fields?",
        "options": ["$reshape", "$modify", "$project", "$transform"],
        "correct_answer": "$project"
    },
    {
        "question": "Which aggregation pipeline stage is used to sort documents?",
        "options": ["$order", "$sort", "$arrange", "$index"],
        "correct_answer": "$sort"
    },
    {
        "question": "Which aggregation pipeline stage is used to limit the number of documents passed to the next stage?",
        "options": ["$restrict", "$limit", "$max", "$cap"],
        "correct_answer": "$limit"
    },
    {
        "question": "Which aggregation pipeline stage is used to deconstruct an array field from the input documents to output a document for each element?",
        "options": ["$explode", "$split", "$unwind", "$flatten"],
        "correct_answer": "$unwind"
    },
    {
        "question": "Which aggregation operator is used to calculate the sum of values?",
        "options": ["$total", "$sum", "$add", "$accumulate"],
        "correct_answer": "$sum"
    },
    {
        "question": "Which aggregation operator is used to calculate the average of values?",
        "options": ["$mean", "$average", "$avg", "$arithmetic"],
        "correct_answer": "$avg"
    },
    {
        "question": "Which aggregate pipeline command is similar to SQL join",
        "options": ["$lookup", "$match", "$group", "$project"],
        "correct_answer": "$lookup"
    },
    {
        "question": "What are the fundamental building blocks of a graph database?",
        "options": ["Tables and rows", "Documents and collections", "Nodes and relationships", "Columns and rows"],
        "correct_answer": "Nodes and relationships"
    },
    {
        "question": "In Neo4j, what does a node represent?",
        "options": ["A relationship between entities", "An entity in the graph", "A property of an entity", "A query in the database"],
        "correct_answer": "An entity in the graph"
    },
    {
        "question": "In Neo4j, what does a relationship represent?",
        "options": ["A property of an entity", "A connection between two entities", "A query in the database", "A constraint on the graph"],
        "correct_answer": "A connection between two entities"
    },
    {
        "question": "What is Cypher?",
        "options": ["A programming language for Neo4j", "A query language for Neo4j", "An operating system for Neo4j", "A data visualization tool for Neo4j"],
        "correct_answer": "A query language for Neo4j"
    },
    {
        "question": "Which Cypher clause is used to find patterns in the graph?",
        "options": ["FIND", "SELECT", "MATCH", "LOCATE"],
        "correct_answer": "MATCH"
    },
    {
        "question": "Which Cypher clause is used to create new nodes and relationships?",
        "options": ["INSERT", "CREATE", "ADD", "MAKE"],
        "correct_answer": "CREATE"
    },
    {
        "question": "Which Cypher clause is used to update the properties of nodes and relationships?",
        "options": ["UPDATE", "MODIFY", "SET", "CHANGE"],
        "correct_answer": "SET"
    },
    {
        "question": "Which Cypher clause is used to delete nodes and relationships?",
        "options": ["REMOVE", "ERASE", "DELETE", "PURGE"],
        "correct_answer": "DELETE"
    },
    {
        "question": "Which Cypher clause is used to specify what data to return from a query?",
        "options": ["DISPLAY", "SHOW", "RETURN", "PRESENT"],
        "correct_answer": "RETURN"
    },
    {
        "question": "Which Cypher clause is used to filter results based on a specified condition?",
        "options": ["FILTER", "WHERE", "HAVING", "CONDITION"],
        "correct_answer": "WHERE"
    },
    {
        "question": "Which command enable to import data from CSV",
        "options": ["IMPORT CSV", "LOAD CSV", "READ CSV", "INSERT CSV"],
        "correct_answer": "LOAD CSV"
    },
    {
        "question": "Which data type is NOT valid in JSON documents?",
        "options": ["String", "Number", "Boolean", "Date"],
        "correct_answer": "Date"
    },
    {
        "question": "What is the advantage of horizontally scaling a NoSQL database?",
        "options": ["Improved read performance on a single machine", "Increased storage capacity across multiple machines", "Simplified data modeling", "Stronger data consistency"],
        "correct_answer": "Increased storage capacity across multiple machines"
    },
    {
        "question": "What is the purpose of the `$exists` operator in MongoDB queries?",
        "options": ["To check if a field is indexed", "To check if a field exists in a document", "To check if a document exists in a collection", "To check if a database exists"],
        "correct_answer": "To check if a field exists in a document"
    },
    {
        "question": "In Cypher, what is used to represent the direction of a relationship?",
        "options": ["A property", "A node", "An arrow", "A constraint"],
        "correct_answer": "An arrow"
    },
    {
        "question": "What is a benefit of NoSQL databases compared to traditional relational databases?",
        "options": ["Strong consistency", "ACID compliance", "Schema flexibility", "Complex transaction support"],
        "correct_answer": "Schema flexibility"
    },
    {
        "question": "What does the 'ACID' acronym stand for in database systems?",
        "options": ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Consistency, Isolation, Durability", "Atomicity, Completeness, Isolation, Durability", "Accuracy, Completeness, Isolation, Durability"],
        "correct_answer": "Atomicity, Consistency, Isolation, Durability"
    },
    {
        "question": "What is eventual consistency?",
        "options": ["A guarantee that data will be consistent immediately after a write operation", "A guarantee that data will never be consistent", "A model where data will become consistent over time", "A model where data is always consistent across all nodes"],
        "correct_answer": "A model where data will become consistent over time"
    },
    {
        "question": "What is the purpose of indexing in NoSQL databases?",
        "options": ["To enforce data consistency", "To optimize query performance", "To reduce storage space", "To simplify data modeling"],
        "correct_answer": "To optimize query performance"
    },
    {
        "question": "In the context of NoSQL databases, what does schema-less mean?",
        "options": ["The database does not store data", "The database has a predefined schema that cannot be changed", "The database has a flexible schema, and each document can have a different structure", "The database requires a schema to be defined before any data can be inserted"],
        "correct_answer": "The database has a flexible schema, and each document can have a different structure"
    },
    {
        "question": "What is the role of the 'localField' and 'foreignField' parameters in MongoDB's `$lookup` stage?",
        "options": ["To specify the collections to join", "To rename fields in the output", "To specify the fields to match on in the local and foreign collections", "To sort the output documents"],
        "correct_answer": "To specify the fields to match on in the local and foreign collections"
    },
    {
        "question": "What is the purpose of the `MERGE` clause in Neo4j Cypher queries?",
        "options": ["To update existing nodes and relationships", "To delete nodes and relationships", "To match existing nodes and relationships or create them if they don't exist", "To return the properties of nodes and relationships"],
        "correct_answer": "To match existing nodes and relationships or create them if they don't exist"
    },
    {
        "question": "Which statement about NoSQL is correct?",
        "options": ["NoSQL databases are always faster than SQL databases", "NoSQL databases can handle unstructured data better than SQL databases", "NoSQL databases always guarantee ACID properties", "NoSQL databases always use a document-oriented model"],
        "correct_answer": "NoSQL databases can handle unstructured data better than SQL databases"
    },
    {
        "question": "What is a common use case for graph databases like Neo4j?",
        "options": ["Storing large volumes of sensor data", "Managing user sessions in a web application", "Analyzing social networks and relationships", "Storing product catalogs"],
        "correct_answer": "Analyzing social networks and relationships"
    },
    {
        "question": "What is the purpose of constraints in Neo4j?",
        "options": ["To improve query performance", "To enforce data integrity and uniqueness", "To manage user access control", "To define data types for node properties"],
        "correct_answer": "To enforce data integrity and uniqueness"
    },
    {
        "question": "In MongoDB, what does the term 'collection' refer to?",
        "options": ["A set of indexes", "A group of related documents", "A stored procedure", "A connection to the database"],
        "correct_answer": "A group of related documents"
    },
    {
        "question": "What is a key advantage of schema-less databases?",
        "options": ["Improved data consistency", "Faster query performance", "Greater flexibility in data structure", "Simplified data modeling"],
        "correct_answer": "Greater flexibility in data structure"
    },
    {
        "question": "What does the term `horizontal scalability` refer to?",
        "options": ["Scaling up the resources on a single server", "Adding more servers to a database system", "Optimizing database queries", "Reducing data redundancy"],
        "correct_answer": "Adding more servers to a database system"
    },
    {
        "question": "What data type is used to store a document in MongoDB?",
        "options": ["XML", "JSON", "CSV", "BSON"],
        "correct_answer": "BSON"
    },
    {
        "question": "Which aggregate function is used to count the number of entries in a group?",
        "options": ["`$sum`", "`$average`", "`$count`", "`$total`"],
        "correct_answer": "`$count`"
    },
    {
        "question": "What is the function of the `LIMIT` clause in Neo4j's Cypher query language?",
        "options": ["To restrict the size of a node's properties", "To filter results based on a maximum value", "To restrict the number of returned relationships", "To limit the number of returned records"],
        "correct_answer": "To limit the number of returned records"
    },
    {
        "question": "Which language is typically used to write queries for Neo4j databases?",
        "options": ["SQL", "CQL", "Cypher", "JavaScript"],
        "correct_answer": "Cypher"
    },
    {
        "question": "What is a constraint in Neo4j?",
        "options": ["A rule that must be followed when querying the database", "A rule that must be followed when creating a new node or property", "A command to import CSV data", "A command to export data"],
        "correct_answer": "A rule that must be followed when creating a new node or property"
    },
    # Code Questions Start Here
    {
        "question": "Given a MongoDB collection `users`, which query would find all users with age greater than 25?",
        "options": ["`db.users.find({ age: > 25 })`", "`db.users.find({ age: { $gt: 25 } })`", "`db.users.find({ age: 'gt 25' })`", "`db.users.find({ age: greaterThan(25) })`"],
        "correct_answer": "`db.users.find({ age: { $gt: 25 } })`"
    },
    {
        "question": "What is the correct Cypher query to create a node with label `Person` and property `name` equal to 'Alice'?",
        "options": ["`CREATE (n:Person { name: 'Alice' })`", "`INSERT (n:Person { name: 'Alice' })`", "`MAKE (n:Person, name='Alice')`", "`NEW (n:Person { name: 'Alice' })`"],
        "correct_answer": "`CREATE (n:Person { name: 'Alice' })`"
    },
    {
        "question": "What is the correct MongoDB aggregation pipeline to group documents by `category` and count the number of documents in each category?",
        "options": ["`db.collection.aggregate([{ group: { _id: '$category', count: { $sum: 1 } } }])`", "`db.collection.aggregate([{ $group: { _id: 'category', count: { $count: 1 } } }])`", "`db.collection.aggregate([{ $group: { _id: '$category', count: { $sum: 1 } } }])`", "`db.collection.aggregate([{ group: { category: '$category', count: { $sum: 1 } } }])`"],
        "correct_answer": "`db.collection.aggregate([{ $group: { _id: '$category', count: { $sum: 1 } } }])`"
    },
    {
        "question": "Which Cypher query is correct to find all friends of 'Alice'?",
        "options": ["`MATCH (alice:Person)-[:FRIEND]-(friend) WHERE alice.name = 'Alice' RETURN friend`", "`MATCH (alice:Person {name: 'Alice'})-->(friend) RETURN friend`", "`MATCH (alice:Person {name: 'Alice'})-[:FRIEND]->(friend) RETURN friend`", "`FIND (alice:Person {name: 'Alice'})-[:FRIEND]-(friend)`"],
        "correct_answer": "`MATCH (alice:Person {name: 'Alice'})-[:FRIEND]->(friend) RETURN friend`"
    },
    {
        "question": "Which MongoDB update command would increment a field named 'views' by 1 for a document with `_id: ObjectId('65eEXAMPLE')`?",
        "options": ["`db.collection.update({ _id: ObjectId('65eEXAMPLE') }, { views: views + 1 })`", "`db.collection.updateOne({ _id: ObjectId('65eEXAMPLE') }, { $set: { views: views + 1 } })`", "`db.collection.updateOne({ _id: ObjectId('65eEXAMPLE') }, { $inc: { views: 1 } })`", "`db.collection.update({ _id: ObjectId('65eEXAMPLE') }, { $inc: { views: 1 } })`"],
        "correct_answer": "`db.collection.updateOne({ _id: ObjectId('65eEXAMPLE') }, { $inc: { views: 1 } })`"
    },
    {
        "question": "Which Cypher command creates a unique constraint on the `email` property of `User` nodes?",
        "options": ["`CREATE UNIQUE CONSTRAINT ON (u:User) ASSERT u.email IS UNIQUE`", "`CREATE CONSTRAINT ON (u:User) REQUIRE u.email IS UNIQUE`", "`CREATE CONSTRAINT FOR (u:User) REQUIRE u.email IS UNIQUE`", "`UNIQUE (u:User) ASSERT u.email IS UNIQUE`"],
        "correct_answer": "`CREATE CONSTRAINT FOR (u:User) REQUIRE u.email IS UNIQUE`"
    },
    {
        "question": "Given the MongoDB aggregation pipeline `db.collection.aggregate([{$match: {status: 'A'}}, {$group: {_id: '$customerId', total: {$sum: '$amount'}}}])`, what does it do?",
        "options": ["Calculates the average amount for each customer with status 'A'", "Filters out customers with status 'A'", "Calculates the total amount for each customer with status 'A'", "Counts the number of customers with status 'A'"],
        "correct_answer": "Calculates the total amount for each customer with status 'A'"
    },
    {
        "question": "Which Cypher query finds all nodes of type 'Movie' that 'Tom Hanks' acted in?",
        "options": ["`MATCH (tom:Person {name: 'Tom Hanks'})-->(movie:Movie) RETURN movie`", "`MATCH (tom:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(movie:Movie) RETURN movie`", "`MATCH (tom:Person {name: 'Tom Hanks'}){ACTED_IN}(movie:Movie) RETURN movie`", "`MATCH (tom:Person {name: 'Tom Hanks'}) AND (movie:Movie) WHERE ACTED_IN RETURN movie`"],
        "correct_answer": "`MATCH (tom:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(movie:Movie) RETURN movie`"
    },
    {
        "question": "What is the outcome of the following MongoDB aggregation pipeline: `db.collection.aggregate([{$project: {name: 1, _id: 0}}])`?",
        "options": ["It renames the `_id` field to `name`", "It returns only the `name` field and excludes the `_id` field", "It excludes the `name` field and includes the `_id` field", "It groups the collection by the `name` field"],
        "correct_answer": "It returns only the `name` field and excludes the `_id` field"
    },
    {
        "question": "Given a Cypher query `MATCH (n {name: 'Example'}) RETURN n`, what does `(n {name: 'Example'})` specify?",
        "options": ["A node labeled 'n' with any properties", "A node labeled 'n' with the property name equal to 'Example'", "A relationship named 'Example'", "A constraint that only allows nodes with the name 'Example'"],
        "correct_answer": "A node labeled 'n' with the property name equal to 'Example'"
    },
    {
        "question": "In MongoDB, how would you specify an index on the `username` field to improve query performance?",
        "options": ["`db.collection.createIndex({ username: 'indexed' })`", "`db.collection.ensureIndex({ username: 1 })`", "`db.collection.index({ username: 1 })`", "`db.collection.createIndex({ username: 1 })`"],
        "correct_answer": "`db.collection.createIndex({ username: 1 })`"
    },
    {
        "question": "Which clause can be used to import nodes from CSV files?",
        "options": ["LOAD CSV", "IMPORT CSV", "READ CSV", "CSV IMPORT"],
        "correct_answer": "LOAD CSV"
    },
    {
        "question": "Which operator do you use in MongoDB to check if at least 1 value from an array is present?",
        "options": ["`$all`", "`$in`", "`$nin`", "`$size`"],
        "correct_answer": "`$in`"
    },
    {
        "question": "What is the correct syntax to order a Cypher query by the `age` property in descending order?",
        "options": ["`SORT BY age DESC`", "`ORDER BY age DESC`", "`ORDER BY age SORT DESC`", "`SORT age DESC`"],
        "correct_answer": "`ORDER BY age DESC`"
    },
    {
        "question": "What is the correct Cypher statement to create an index",
        "options": ["`CREATE INDEX FOR (n:movie) ON (n.title)`", "`CREATE PROPERTY INDEX FOR (n:movie) ON (n.title)`", "`CREATE BTREE INDEX FOR (n:movie) ON (n.title)`", "`INDEX {n:movie} ON (n.title)`"],
        "correct_answer": "`CREATE PROPERTY INDEX FOR (n:movie) ON (n.title)`"
    },
    {
        "question": "What operator could enable you to extract only a subset of a particular array",
        "options": ["`$filter`", "`$slice`", "`$range`", "`$limit`"],
        "correct_answer": "`$slice`"
    },
    {
        "question": "Regarding uniqueness, what is the correct Cypher statement to create an uniqueness constrait",
        "options": ["`CREATE CONSTRAINT IF NOT EXISTS FOR (n:Person) REQUIRE n.email IS UNIQUE`", "`CREATE CONSTRAINT IF NOT EXISTS FOR (n:Person) ASSERT n.email IS UNIQUE`", "`CREATE CONSTRAINT FOR (n:Person) REQUIRE n.email IS UNIQUE`", "`CREATE UNIQUE IF NOT EXISTS FOR (n:Person) REQUIRE n.email IS UNIQUE`"],
        "correct_answer": "`CREATE CONSTRAINT IF NOT EXISTS FOR (n:Person) REQUIRE n.email IS UNIQUE`"
    },
    {
        "question": "In MongoDB, what statement would you use to insert many elements?",
        "options": ["`insertAll`", "`insert`", "`insertMany`", "`insert_many`"],
        "correct_answer": "`insertMany`"
    },
    {
        "question": "In Neo4j, what would be the appropriate statement to verify existing and creating it if doesn't exist",
        "options": ["`CREATE`", "`INSERT`", "`MERGE`", "`CHECK`"],
        "correct_answer": "`MERGE`"
    },
    {
        "question": "You are using the aggregate, which statement would select the field `city`",
        "options": ["`match`", "`select`", "`group`", "`where`"],
        "correct_answer": "`match`"
    },
    {
        "question": "Which is not a step to import a `CSV` file",
        "options": ["`LOAD CSV WITH HEADERS FROM 'file:///path/to/mydata.csv' AS row`", "`MERGE (p:Person { id: row.personId, name: row.name })`", "`CREATE (p:Person { id: row.personId, name: row.name })`", "`(line in lines)`"],
        "correct_answer": "`(line in lines)`"
    },
    {
        "question": "Which statement can be used to update a field",
        "options": ["`WHERE`", "`MODIFY`", "`SET`", "`ALTER`"],
        "correct_answer": "`SET`"
    },
    {
        "question": "What is the result of the following MongoDB query? `db.products.insertMany([{id: 10, item: 'large box', qty: 20}, {id: 11, item: 'small box', qty: 55}, {id: 12, item: 'medium box', qty: 30}])`",
        "options": [
            "{ 'acknowledged': true, 'insertedIds': [ObjectId('612497c67c058c794cbf5482'), ObjectId('614497c67c058c794cbf5483'), 12] }",
            "{ 'acknowledged': true, 'insertedIds': [10, 11, 12] }",
            "{ 'acknowledged': true, 'insertedIds': [ObjectId('612497c67c058c794cbf5482'), ObjectId('612497c67c058c794cbf5483'), ObjectId('61a497c67c058c794cbf5484')] }",
            "{ 'acknowledged': true, 'insertedIds': [10, 11, ObjectId('614497c67c058c794cbf5484')] }"
        ],
        "correct_answer": "{ 'acknowledged': true, 'insertedIds': [ObjectId('612497c67c058c794cbf5482'), ObjectId('614497c67c058c794cbf5483'), 12] }"
    },
    {
        "question": "Which MongoDB aggregation query correctly joins documents from 'orders' with those from 'inventory'?",
        "options": [
            """db.orders.aggregate([ { $lookup: { to: 'inventory', localField: 'sku', primaryField: 'item', as: 'inventory_docs' } } ])""",
            """db.orders.aggregate([ { $lookup: { to: 'inventory', localField: 'item', primaryField: 'sku', as: 'inventory_docs' } } ])""",
            """db.orders.aggregate([ { $lookup: { from: 'inventory', localField: 'sku', foreignField: 'item', as: 'inventory_docs' } } ])""",
            """db.orders.aggregate([ { $lookup: { from: 'inventory', localField: 'item', foreignField: 'sku', as: 'inventory_docs' } } ])"""
        ],
        "correct_answer": """db.orders.aggregate([ { $lookup: { from: 'inventory', localField: 'item', foreignField: 'sku', as: 'inventory_docs' } } ])"""
    },
    {
        "question": "Which MongoDB deleteOne() method statement is correct?",
        "options": [
            "Allows you to delete a single document",
            "Returns an error if the specified filter does not match any documents",
            "Can be used to delete all documents in a collection",
            "Returns a document (result object)"
        ],
        "correct_answer": "Allows you to delete a single document"
    },
    {
        "question": "Which MongoDB query is equivalent to `SELECT * FROM inventory WHERE status = 'A' AND qty < 30`?",
        "options": [
            "db.inventory.find({ status: 'A', qty: { $lt: 30 } })",
            "db.inventory.find({ { status: 'A' } & { qty: { $lt: 30 } } })",
            "db.inventory.find({ $and: [ { status: 'A' }, { qty: { $lt: 30 } } ] })",
            "db.inventory.find({ { status: 'A' } / { qty: { $lt: 30 } } })"
        ],
        "correct_answer": "db.inventory.find({ $and: [ { status: 'A' }, { qty: { $lt: 30 } } ] })"
    },
    {
        "question": "Which MongoDB aggregation query is equivalent to `SELECT cust_id, SUM(li.qty) AS qty FROM orders o, order_lineitem li WHERE li.order_id = o.id GROUP BY cust_id`?",
        "options": [
            "db.orders.aggregate([{ $unwind: '$items' }, { $group: { _id: '$cust_id', qty: { $sum: '$items.qty' } } } ])",
            "db.orders.aggregate([{ $slice: '$items' }, { $group: { _id: '$cust_id', qty: { $sum: '$items.qty' } } } ])",
            "db.orders.aggregate([{ $unwind: '$items' }, { $group: { _id: 'cust_id', qty: { $sum: '$items.qty' } } } ])",
            "db.orders.aggregate([{ $slice: '$items' }, { $group: { _id: 'cust_id', qty: { $sum: '$items.qty' } } } ])"
        ],
        "correct_answer": "db.orders.aggregate([{ $unwind: '$items' }, { $group: { _id: '$cust_id', qty: { $sum: '$items.qty' } } } ])"
    },
    {
        "question": "Which operators below can be used in an updateMany() operation?",
        "options": [
            "$set",
            "$lookup",
            "$unionWith",
            "$unset"
        ],
        "correct_answer": "$set"
    },
    {
        "question": "Which MongoDB query would return a single document with `_id: 10, bar: 'abc'` if it exists?",
        "options": [
            "insertOne({ foo: 'abc' })",
            "insertOne({ _id: 10, bar: 'abc' })",
            "insertOne({ _id: 20, foo: 'abc' })",
            "insertOne({ bar: 'abc' })"
        ],
        "correct_answer": "insertOne({ bar: 'abc' })"
    },
    {
        "question": "What is the role of the aggregation pipeline?",
        "options": ["`Optimize queries`", "`Validate data integrity`", "`Transform and aggregate data`", "`Manage indexes`"],
        "correct_answer": "`Transform and aggregate data`"
    },
    {
        "question": "What statement could validate if a given field exists, for exemple `email`",
        "options": ["`$TYPE`", "`$CHECK`", "`$EXISTS`", "`$VALIDATE`"],
        "correct_answer": "`$EXISTS`"
    },
    {
        "question": "You are using the function `db.collection.find({city:{$in:['Paris','London']}})`, what could be a good alternative to `$IN`",
        "options": ["`$AND`", "`$SIZE`", "`$EQ`", "`$OR`"],
        "correct_answer": "`$OR`"
    },
    {
        "question": "You use `{{$group:{{_id:'$city', total_population:{{$sum:'$population'}}}}}}`, what can you say?",
        "options": ["`Returns the size for each city`", "`Returns all the document`", "`Returns the city and population`", "`Returns an error`"],
        "correct_answer": "`Returns an error`"
    },
    {
        "question": "Which function permit to join 2 collections?",
        "options": ["`$JOIN`", "`$LINK`", "`$LOOKUP`", "`$RELATION`"],
        "correct_answer": "`$LOOKUP`"
    },
    {
        "question": "In MongoDB, what would be the correct code to find all documents where the 'status' field is equal to 'active'?",
        "options": ["`db.collection.find({ status: 'active' })`", "`db.collection.select({ status: 'active' })`", "`db.collection.query({ status: 'active' })`", "`db.collection.get({ status: 'active' })`"],
        "correct_answer": "`db.collection.find({ status: 'active' })`"
    },
    {
        "question": "In Neo4j, what Cypher code snippet would you use to find all nodes related to a node named 'John'?",
        "options": ["`FIND (john:Person {name: 'John'})-->(related)`", "`MATCH (john:Person {name: 'John'})-->(related) RETURN related`", "`SEARCH (john:Person {name: 'John'})-->(related)`", "`SELECT related FROM (john:Person {name: 'John'})`"],
        "correct_answer": "`MATCH (john:Person {name: 'John'})-->(related) RETURN related`"
    },
    {
        "question": "Suppose you have a MongoDB document with an array called 'tags'. Which code snippet would add the value 'featured' to the 'tags' array if it's not already present?",
        "options": ["`db.collection.update({_id: docId}, {$push: {tags: 'featured'}})`", "`db.collection.update({_id: docId}, {$addToSet: {tags: 'featured'}})`", "`db.collection.update({_id: docId}, {$add: {tags: 'featured'}})`", "`db.collection.update({_id: docId}, {$set: {tags: 'featured'}})`"],
        "correct_answer": "`db.collection.update({_id: docId}, {$addToSet: {tags: 'featured'}})`"
    },
    {
        "question": "In Cypher, what's wrong about the statement `CREATE INDEX ON:Movie(title);`",
        "options": ["The Movie is a property, not a Node", "There's no wrong, the code is correct", "The Syntax is not correct", "There's no need for an index"],
        "correct_answer": "The Syntax is not correct"
    },
    {
        "question": "What is wrong about the query `db.movies.update({name:{$exists:true}},{$set:{name:'a'}},{multi:true});`",
        "options": ["`multi` is not a valid flag, it should be all", "Nothing is wrong", "It should be `multi:True`", "It should be `multiple:true`"],
        "correct_answer": "It should be `multi:True`"
    },
]

def check_answer(question, selected_answer):
    return selected_answer == question["correct_answer"]

def display_question(question, question_number, correct_count):
    st.write(f"**Question {question_number + 1} / {st.session_state.num_questions}**")
    st.write(f"Correct Answers: {correct_count}")
    st.write(f"**{question['question']}**")
    selected_answer = st.radio("Choose an answer:", question["options"])
    return selected_answer

# Function to display PDF
def displayPDF(file):
    # Read file as bytes:
    bytes_data = file.read()

    # Convert to base64:
    base64_pdf = base64.b64encode(bytes_data).decode('utf-8')

    # Embed PDF in HTML:
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Display file
    st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("NoSQL Exam Practice")

    # Initialize session state
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.num_questions = 10  # Default number of questions
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.questions_order = list(range(len(questions)))
        random.shuffle(st.session_state.questions_order)
        st.session_state.results = []  # Store results for the summary

    # Sidebar for course PDF and settings
    with st.sidebar:
        st.header("Course Materials")
        pdf_file = st.file_uploader("Upload Course PDF", type=["pdf"])
        if pdf_file is not None:
            displayPDF(pdf_file)

    # Main area for the quiz
    col1, col2 = st.columns([3, 1]) #Adjust columns width
    with col1:
        num_questions = st.number_input("Enter the number of questions for this quiz:", min_value=1, max_value=len(questions), value=st.session_state.num_questions, step=1)

        # Max Questions button
        if st.button("Max Questions"):
            num_questions = len(questions)  # Set to the maximum number of questions

        st.session_state.num_questions = int(num_questions)

        question_index = st.session_state.question_index
        questions_order = st.session_state.questions_order
        correct_count = st.session_state.score

        if question_index < st.session_state.num_questions:
            question = questions[questions_order[question_index]]
            selected_answer = display_question(question, question_index, correct_count)

            if st.button("Submit"):
                if selected_answer:
                    is_correct = check_answer(question, selected_answer)
                    if is_correct:
                        st.success("Correct!")
                        st.session_state.score += 1
                        st.session_state.results.append({"question": question["question"], "correct": True, "correct_answer": question["correct_answer"], "selected_answer": selected_answer})
                    else:
                        st.error(f"Incorrect. The correct answer was: {question['correct_answer']}")
                        st.session_state.results.append({"question": question["question"], "correct": False, "correct_answer": question["correct_answer"], "selected_answer": selected_answer})

                    st.session_state.question_index += 1
                    st.rerun()  # Rerun to display the next question
                else:
                    st.warning("Please select an answer.")
        else:
            st.header("Quiz Complete!")
            st.write(f"Your final score: {st.session_state.score} / {st.session_state.num_questions}")

            # Display Summary
            st.subheader("Review")
            for result in st.session_state.results:
                st.write(f"**Question:** {result['question']}")
                st.write(f"  * Your Answer: {result['selected_answer']}")
                st.write(f"  * Correct Answer: {result['correct_answer']}")
                if result['correct']:
                    st.success("   * Correct!")
                else:
                    st.error("   * Incorrect")

            if st.button("Restart Quiz"):
                st.session_state.question_index = 0
                st.session_state.score = 0
                st.session_state.questions_order = list(range(len(questions)))
                random.shuffle(st.session_state.questions_order)
                st.session_state.results = [] #Clears the results
                st.rerun()

if __name__ == "__main__":
    main()

