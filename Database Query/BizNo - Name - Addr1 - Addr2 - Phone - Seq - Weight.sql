SELECT FoodCorp.BizNo, FoodCorp.Name, FoodCorp.Addr1, FoodCorp.Addr2, Member.Phone, FoodWaste.Seq, FoodWaste.Weight, FoodCorp.RegistDate
FROM
    (Member LEFT JOIN FoodCorp ON Member.MemberID = FoodCorp.MemberId
    LEFT JOIN FoodWaste ON Member.MemberID = FoodWaste.MemberID)
WHERE Member.Role != 'admin' AND Member.Type != 'clean';