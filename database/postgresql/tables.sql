CREATE TYPE STATE AS ENUM ('OPEN', 'CLOSED', 'REOPENED');

CREATE TABLE IF NOT EXISTS REPOS (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    stargazers_count INT NOT NULL,
    forks_count INT NOT NULL,
    open_issues_count INT NOT NULL,
    watchers_count INT NOT NULL,
    tags VARCHAR(255),
    topics VARCHAR(255),
    owner VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS ISSUES (
    id BIGINT PRIMARY KEY,
    number INT NOT NULL,
    repo_id BIGINT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(1000),
    opened_by VARCHAR(255) NOT NULL,
    opened_at TIMESTAMP NOT NULL,
    assignee VARCHAR(255),
    comments VARCHAR(255),
    labels VARCHAR(255),
    milestone VARCHAR(255),
    sub_issues_summary VARCHAR(255),
    current_status STATE DEFAULT 'OPEN' NOT NULL,
    FOREIGN KEY (repo_id) REFERENCES REPOS(id)
);

CREATE TABLE IF NOT EXISTS LANGUAGES (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS REPO_LANGUAGE_MAPPINGS (
    id BIGINT PRIMARY KEY,
    repo_id BIGINT NOT NULL,
    language_id BIGINT NOT NULL,
    FOREIGN KEY (repo_id) REFERENCES REPOS(id),
    FOREIGN KEY (language_id) REFERENCES LANGUAGES(id)
);
