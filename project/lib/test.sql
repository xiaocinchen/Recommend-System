create PROCEDURE querymore(textname varchar(30)) 

BEGIN

  set @textname = CONCAT(textname); 

--   set @tablename = CONCAT('select label from news where textname = ','''', @textname,'''',';');
  set @cnt = (select count(*) from user);
  select @cnt;

--   select @tablename;

  set @sql = CONCAT('select * from ',@tablename);

  prepare stmt from @sql; 

  execute stmt ; 

  deallocate prepare stmt;

END;
