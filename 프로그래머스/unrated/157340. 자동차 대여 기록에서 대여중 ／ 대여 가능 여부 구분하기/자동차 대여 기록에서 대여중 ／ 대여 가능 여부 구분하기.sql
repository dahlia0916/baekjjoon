-- 코드를 입력하세요
SELECT distinct CAR_ID, if(CAR_ID in 
                          (SELECT CAR_ID
                          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                          WHERE '2022-10-16' between START_DATE and END_DATE),"대여중","대여 가능") as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
order by CAR_ID desc

