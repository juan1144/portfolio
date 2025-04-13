CREATE SCHEMA IF NOT EXISTS django AUTHORIZATION postgres;
ALTER ROLE postgres SET search_path TO django;
