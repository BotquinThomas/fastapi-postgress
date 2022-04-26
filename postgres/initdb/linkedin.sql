CREATE TABLE IF NOT EXISTS linkedin_job_posts (
    id SERIAL PRIMARY KEY,
    role VARCHAR(50),
    job_description text
);