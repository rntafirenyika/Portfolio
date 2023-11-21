CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    category TEXT NOT NULL);
CREATE TABLE countries(
    country_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    country_name TEXT NOT NULL);
CREATE TABLE genders(
    gender_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  
    gender TEXT NOT NULL);
CREATE TABLE activity(
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    activity_status TEXT NOT NULL);
CREATE TABLE titles(
    title_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title TEXT NOT NULL);
CREATE TABLE users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    gender_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    cell_number TEXT,
    email TEXT NOT NULL,
    country_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    notes TEXT,
    hash TEXT NOT NULL,
    dt_stamp DEFAULT (datetime('now', 'localtime')),
    encrypted_key TEXT,
    datekey TEXT,
    userrole TEXT,
    FOREIGN KEY(country_id) REFERENCES countries(country_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id),
    FOREIGN KEY(activity_id) REFERENCES activity(activity_id),
    FOREIGN KEY(title_id) REFERENCES titles(title_id));
CREATE TABLE emaillist(
    email_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    email TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    activity_id INTEGER,
    FOREIGN KEY(country_id) REFERENCES countries(country_id),
    FOREIGN KEY(category_id) REFERENCES categories(category_id));
CREATE TABLE wip(
    wip_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    email_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    DTStamp DEFAULT (datetime('now', 'localtime')),
    utcDTStamp DEFAULT (datetime('now', 'utc')),
    wip_status TEXT NOT NULL,
    wip_type TEXT NOT NULL,
    wip_subject TEXT NOT NULL,
    wip_message TEXT NOT NULL,
    cv_name TEXT,
    cv_type TEXT,
    cv_data BLOB,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(email_id) REFERENCES emaillist(email_id),
    FOREIGN KEY(country_id) REFERENCES countries(country_id),
    FOREIGN KEY(category_id) REFERENCES categories(category_id));
CREATE TABLE documents(
    document_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    filename TEXT,
    file_type TEXT,
    filedata BLOB,
    DTStamp DEFAULT (datetime('now', 'localtime')),
    utcDTStamp DEFAULT (datetime('now', 'utc')),
    FOREIGN KEY(user_id) REFERENCES users(user_id));
CREATE TABLE history(
    hist_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    hist_subject TEXT NOT NULL,
    email TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    DTStamp DEFAULT (datetime('now', 'localtime')),
    utcDTStamp DEFAULT (datetime('now', 'utc')),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(category_id) REFERENCES categories(category_id),
    FOREIGN KEY(country_id) REFERENCES countries(country_id));

CREATE INDEX Uemail ON users (email);
CREATE INDEX Lemail ON emaillist (email);