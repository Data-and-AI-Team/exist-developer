---
name: react-developer
description: Use when developing, reviewing, or providing architectural guidance for React applications.
---

# React Developer

Use the skills and guidance from:

https://react.dev/

## Pagination Requirements

All APIs that return list-like data must return paginated data using Spring Data's `Page<T>` interface. React clients must model and consume the resulting page response, including its content and pagination metadata, rather than expecting a bare array.

React services/hooks consuming list-like APIs must accept pagination parameters (`page`, `size`, and optional `sort`), send them with the request, and return typed models matching the serialized Spring `Page<T>` response. Clients must not unwrap `content` into a bare array or discard pagination metadata.
