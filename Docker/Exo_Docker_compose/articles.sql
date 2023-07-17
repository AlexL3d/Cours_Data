CREATE DATA IF NOT EXISTS test;

USE test;

CREATE TABLE IF NOT EXISTS articles (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    date_published TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content TEXT NULL,
    PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;