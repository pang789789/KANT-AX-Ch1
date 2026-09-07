-- AX 2회차 Ch 1: PostgreSQL 회원관리 과제
-- 빈 실습 데이터베이스에서 전체를 위에서부터 실행한다.
-- 같은 practice.members 테이블이 이미 있으면 CREATE TABLE에서 중단된다.
-- 기존 데이터를 삭제하는 초기화 구문은 포함하지 않았다.
BEGIN;

-- Part 1. Schema와 Table 생성
CREATE SCHEMA IF NOT EXISTS practice;
CREATE TABLE practice.members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    joined_at DATE
);

SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'practice' AND table_name = 'members'
ORDER BY ordinal_position;

-- Part 2. 회원 5명 입력 및 조회 (모두 가상 데이터)
INSERT INTO practice.members (name, email, age, joined_at) VALUES
('김민수', 'minsu@example.com', 25, '2026-08-01'),
('이지은', 'jieun@example.com', 22, '2026-08-03'),
('박서준', 'seojun@example.com', 35, '2026-08-05'),
('최유나', 'yuna@example.com', 28, '2026-08-10'),
('정도현', 'dohyun@example.com', 19, '2026-08-15');
SELECT * FROM practice.members ORDER BY member_id;
SELECT name, email FROM practice.members ORDER BY member_id;
SELECT * FROM practice.members WHERE age >= 25 ORDER BY member_id;
SELECT * FROM practice.members WHERE name = '이지은' ORDER BY member_id;
SELECT * FROM practice.members ORDER BY age DESC, member_id;
SELECT * FROM practice.members ORDER BY joined_at ASC, member_id;

-- Part 3. 변경 대상을 먼저 조회하고, 변경 후 결과 확인
SELECT * FROM practice.members WHERE member_id = 1;
UPDATE practice.members SET age = 30 WHERE member_id = 1;
SELECT * FROM practice.members WHERE member_id = 1;
SELECT * FROM practice.members WHERE member_id = 5;
DELETE FROM practice.members WHERE member_id = 5;
SELECT * FROM practice.members ORDER BY member_id;

-- Part 4. 변경 완료 후 남은 회원을 기준으로 집계
SELECT COUNT(*) AS member_count FROM practice.members;
SELECT ROUND(AVG(age), 2) AS average_age FROM practice.members;
SELECT MAX(age) AS oldest_age FROM practice.members;
SELECT MIN(age) AS youngest_age FROM practice.members;
SELECT COUNT(*) AS members_25_or_older FROM practice.members WHERE age >= 25;

-- 도전 1. 정수 나이를 10으로 나누어 연령대를 계산
SELECT (age / 10) * 10 AS age_group, COUNT(*) AS member_count
FROM practice.members GROUP BY (age / 10) * 10 ORDER BY age_group;

-- 도전 2. 가장 최근에 가입한 회원
SELECT * FROM practice.members ORDER BY joined_at DESC NULLS LAST, member_id DESC LIMIT 1;

-- 도전 3. 평균 나이보다 나이가 많은 회원
SELECT * FROM practice.members
WHERE age > (SELECT AVG(age) FROM practice.members) ORDER BY age DESC, member_id;

-- 도전 4. 이메일로 검색
SELECT * FROM practice.members WHERE email = 'jieun@example.com';

-- 도전 5. 조건 두 개를 함께 사용
SELECT * FROM practice.members WHERE age >= 25 AND joined_at >= DATE '2026-08-05'
ORDER BY member_id;

COMMIT;
