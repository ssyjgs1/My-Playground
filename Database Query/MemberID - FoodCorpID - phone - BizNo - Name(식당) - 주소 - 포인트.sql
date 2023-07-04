SELECT Member.MemberID, FoodCorp.FoodCorpID, Member.phone, FoodCorp.BizNo, FoodCorp.Name, FoodCorp.Addr1, FoodCorp.Addr2, Member.point
FROM Member
JOIN FoodCorp ON Member.MemberID = FoodCorp.MemberID
WHERE Member.Role <> 'admin' AND Member.Type <> 'clean';