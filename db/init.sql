CREATE DATABASE oscarmaleData;
use oscarmaleData;

CREATE TABLE IF NOT EXISTS oscar_age_male (
    `id` int AUTO_INCREMENT,
    `Year` INT,
    `Age` INT,
    `Name` VARCHAR(25) CHARACTER SET utf8,
    `Movie` VARCHAR(34) CHARACTER SET utf8,
    PRIMARY KEY (`id`)
);
INSERT INTO oscar_age_male (Year,Age,Name,Movie) VALUES
    (1928,44,'Emil Jannings','The Last Command'),
    (1929,41,'Warner Baxter','In Old Arizona'),
    (1930,62,'George Arliss','Disraeli'),
    (1931,53,'Lionel Barrymore','A Free Soul'),
    (1932,47,'Wallace Beery','The Champ'),
    (1933,35,'Fredric March','Dr. Jekyll and Mr. Hyde'),
    (1934,34,'Charles Laughton','The Private Life of Henry VIII'),
    (1935,34,'Clark Gable','It Happened One Night'),
    (1936,49,'Victor McLaglen','The Informer'),
    (1937,41,'Paul Muni','The Story of Louis Pasteur'),
    (1938,37,'Spencer Tracy','Captains Courageous'),
    (1939,38,'Spencer Tracy','Boys Town'),
    (1940,34,'Robert Donat','Goodbye'),
    (1941,32,'James Stewart','The Philadelphia Story'),
    (1942,40,'Gary Cooper','Sergeant York'),
    (1943,43,'James Cagney','Yankee Doodle Dandy'),
    (1944,48,'Paul Lukas','Watch on the Rhine'),
    (1945,41,'Bing Crosby','Going My Way'),
    (1946,39,'Ray Milland','The Lost Weekend'),
    (1947,49,'Fredric March','The Best Years of Our Lives'),
    (1948,57,'Ronald Colman','A Double Life'),
    (1949,41,'Laurence Olivier','Hamlet'),
    (1950,38,'Broderick Crawford','All the King''s Men');
