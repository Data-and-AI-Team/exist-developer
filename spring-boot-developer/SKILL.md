---
name: spring-boot-developer
description: Use when developing, reviewing, or providing architectural guidance for Spring Boot applications.
---

# Spring Boot Developer

Use the skills and guidance from:

https://github.com/rrezartprebreza/spring-boot-skills

## Requirements

All APIs that return list-like results must accept pagination parameters and return paginated results using Spring Data's `Page<T>` interface. Do not return an unbounded `List<T>`, `Collection<T>`, array, or other bare collection from these endpoints. Prefer accepting Spring Data's `Pageable` to support page, size, and sort parameters.