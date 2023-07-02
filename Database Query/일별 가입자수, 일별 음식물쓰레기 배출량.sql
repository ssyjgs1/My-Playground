-- 일별 가입자 수 계산
SELECT DATE_FORMAT(RegistDate, '%Y-%m-%d') AS DATE, COUNT(*) AS num
FROM Member
GROUP BY DATE;

-- 일별 쓰레기 배출량 계산
SELECT DATE_FORMAT(RegistDate, '%Y-%m-%d') AS DATE, sum(weight) AS num
FROM CleanLog
GROUP BY DATE;