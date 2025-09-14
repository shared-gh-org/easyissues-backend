-- Insert dummy repos
INSERT INTO REPOS (id, name, description, stargazers_count, forks_count, open_issues_count, watchers_count, tags, topics, owner)
VALUES
    (1, 'easyissues', 'Simple issue tracker', 42, 10, 3, 50, 'bug,feature', 'tracking,management', 'alice'),
    (2, 'coolproject', 'Cool project for testing', 100, 20, 5, 200, 'open-source,cli', 'tools,utility', 'bob');

-- Insert dummy issues
INSERT INTO ISSUES (id, number, repo_id, title, description, opened_by, opened_at, assignee, comments, labels, milestone, sub_issues_summary, current_status)
VALUES
    (101, 1, 1, 'First bug', 'There is a small bug in the UI', 'charlie', NOW(), 'david', 'Needs review', 'bug,UI', 'v1.0', 'None', 'OPEN'),
    (102, 2, 1, 'Add dark mode', 'Implement dark mode for better UX', 'eve', NOW(), NULL, NULL, 'feature,UI', 'v2.0', 'None', 'OPEN'),
    (103, 1, 2, 'Improve CLI speed', 'Optimize CLI startup time', 'frank', NOW(), 'grace', 'Performance discussion', 'enhancement,performance', 'v1.1', 'None', 'CLOSED');

-- Insert dummy languages
INSERT INTO LANGUAGES (id, name)
VALUES
    (1, 'Python'),
    (2, 'JavaScript'),
    (3, 'Go');

-- Map repos to languages
INSERT INTO REPO_LANGUAGE_MAPPINGS (id, repo_id, language_id)
VALUES
    (1, 1, 1),  -- easyissues -> Python
    (2, 1, 2),  -- easyissues -> JavaScript
    (3, 2, 3);  -- coolproject -> Go
