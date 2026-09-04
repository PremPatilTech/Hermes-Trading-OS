# Security Policy

## Public Boundary

Hermes Trading OS is a public-safe case study. The public boundary is strict:

- no credentials
- no account identifiers
- no broker server identifiers
- no exact symbols
- no production endpoints
- no private infrastructure paths
- no real execution logs
- no proprietary strategy thresholds

## Reporting a Security Issue

If a sensitive value is accidentally discovered in this repository, open a private channel with the repository owner before creating a public issue.

## Maintainer Checklist

Before publishing any new artifact:

1. Search for credentials, account IDs, hostnames, IP addresses, and tokens.
2. Confirm mock data is clearly marked as illustrative.
3. Confirm diagrams do not include private deployment paths.
4. Confirm docs do not reveal exact strategy thresholds or execution parameters.
5. Confirm generated reports contain no real account, broker, or ticket data.

