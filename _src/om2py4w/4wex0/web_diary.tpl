<html>
<head><title>MyDearDiary-web</title></head>
<body>
<h2>输入日记内容:</h2>
<form action="/mydiary" method="GET">
<input type="text" size="100" maxlength="100" name="content">
<input type="submit" name="save" value="save">
</form>
<br />
<h3>历史记录</h3>
<table border='1'>
%for row in rows:
	<tr>
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>
</body>
</html>


