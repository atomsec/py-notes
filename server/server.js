const net = require('net');

net.createServer( res => {
  res.write('连接服务器成功!')
  res.on('data', function(data){
    res.write(data)
  })
  res.on('end', function(){
    console.log('end');
  })
}).listen(4000)