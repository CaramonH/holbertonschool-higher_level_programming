-- Check if user_0d_1 already exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1') INTO @user_exists;

-- Create user_0d_1 if it doesn't exist
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_1 created with all privileges.';
ELSE
    SELECT 'User user_0d_1 already exists. Skipping user creation.';
END IF;