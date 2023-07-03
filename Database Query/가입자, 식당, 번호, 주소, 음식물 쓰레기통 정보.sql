SELECT
    Member.MemberID,
    Member.Name,
    FoodCorp.Name,
    Member.Phone,
    Member.Email,
    FoodCorp.Addr1,
    FoodCorp.Addr2,
    FoodCorp.BizNo,
    FoodWaste.Seq,
    FoodWaste.Weight,
    Member.Status,
    Member.Role,
    Member.Type,
    Member.Payment,
    Member.PaymentType,
    Member.Point,
    Member.RegistDate,
    Member.LastUpdate,
    Member.IsPush,
    Member.IsSms,
    Member.IsEmail,
    Member.IsEnabled
FROM
    (Member LEFT JOIN FoodCorp ON Member.MemberID = FoodCorp.MemberId)
    LEFT JOIN FoodWaste ON Member.MemberID = FoodWaste.MemberID