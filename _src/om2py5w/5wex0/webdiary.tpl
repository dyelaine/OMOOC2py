<!DOCTYPE html>
<html>
  <head>
    <title>The Dear Diary</title>
  </head>
  <body>
    <h1>The Dear Diary</h1>
    <form action="/" method="post">
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="save" type="submit">保存</button></div>
    </form>
    <h2>历史日记:</h2>
    %import time
    %count = 0
    %for row in rows:
      %count = count +1
        <div class=post>
          <em class=date>{{row['time']}}</em><br>
          {{!row['content'].replace('\n','<br/>')}}
        </div>
    %end
    <h4>当前日记的数目: {{count}} </h4>
  </body>
</html>