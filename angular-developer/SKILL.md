---
name: angular-developer
description: Use when developing, reviewing, or providing architectural guidance for Angular applications.
---

# Angular Developer

Use the skills and guidance from:

https://github.com/angular/skills/tree/main

## Application Naming

Name Angular application modules using the `<app-name>-ui` convention. Do not use generic names such as `frontend`, `web`, or `client` when creating an Angular application module.

## Deployment Environments

When frontend behavior must differ between AWS Lambda and Kubernetes deployments, use `src/environments/environment.lambda.ts` and `src/environments/environment.k8.ts`. Select them with Angular build-configuration `fileReplacements`; do not infer the deployment target from missing runtime configuration or scatter target checks through components and services.

Keep secrets and values that must change after the image is built out of Angular environment files. Use runtime configuration for public endpoints, OAuth client metadata, and other non-secret deploy-time values.

## Pagination Requirements

All APIs that return list-like data must return paginated data using Spring Data's `Page<T>` interface. Angular clients must model and consume the resulting page response, including its content and pagination metadata, rather than expecting a bare array.

Angular services consuming list-like APIs must accept pagination parameters (`page`, `size`, and optional `sort`), send them with the request, and return a typed Angular page model matching the serialized Spring `Page<T>` response (for example, `Observable<Page<T>>`). Services must not unwrap `content` into a bare array or discard pagination metadata.
