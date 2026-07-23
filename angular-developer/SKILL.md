---
name: angular-developer
description: Use when developing, reviewing, or providing architectural guidance for Angular applications.
---

# Angular Developer

Use the skills and guidance from:

https://github.com/angular/skills/tree/main

## Pagination Requirements

All APIs that return list-like data must return paginated data using Spring Data's `Page<T>` interface. Angular clients must model and consume the resulting page response, including its content and pagination metadata, rather than expecting a bare array.

Angular services consuming list-like APIs must accept pagination parameters (`page`, `size`, and optional `sort`), send them with the request, and return a typed Angular page model matching the serialized Spring `Page<T>` response (for example, `Observable<Page<T>>`). Services must not unwrap `content` into a bare array or discard pagination metadata.
