
var sectionNo=1;
var status;

$(document).on('click','#foldersData',function(event){	
	var folderName = $(this).data('folder');  
  var path = $(this).data('item');
  var subFolder = '#'+folderName;  
  if($(this).find(subFolder).find('li').length==0)
  {
    console.log("if part --0");
    $.ajax({
    type:'POST',
      url: '/subDetails/',
      data: {folderName:path},
      success: function( response ) {
          // console.log("success"); // server response 
          if(subFolder.length!=0)
          {
            for(var i = 0; i < response.folder.length; i++)
            {
              var list = '<li id="foldersData" class="glyphicon glyphicon glyphicon-play" data-folder = '+response.folder[i]+' data-item = '+path+'/'+response.folder[i]+'>'+response.folder[i]+'<ul id = '+response.folder[i]+'></ul></li><br>';
              $(subFolder).append(list);
            }
            for(var i = 0; i < response.files.length; i++)
            {              
              var link="existing#"+path+"/"+response.files[i];
              // console.log(path+"/"+response.files[i]); onclick="openTab(this.id)"
              var list = '<li id='+link+' onclick="openTab(this.id)">'+response.files[i]+'</li>';              
              $(subFolder).append(list);
            }
          }
      }
      });
  }
  else
  {
    console.log("else part --0 "+$(this).id);    
  }
  event.stopPropagation();
});
$("#create").click(function(){
  // alert("ckm");
  var id="newFile#codeanywhere/templates/static/"+$("#filenameExtension").val();
  console.log(id);
  openTab(id);
  // alert(id);
});

function openTab(id)
{
  console.log("clicked path is  "+id);
  id=id.split('#');
  status=id[0];
  id=id[1];
  console.log(status +" and "+ id);
  if(id.indexOf("codeanywhere") !=-1)
  {
    text=id.replace("codeanywhere","");  
    if(text.indexOf("/templates") !=-1)
    {
      text=text.replace("/templates","");
      console.log("loading from path "+text);
    }    
    var filename=text.split("/").pop();
    console.log("poped file name "+filename);
    var activateMode=filename.split(".").pop();
    console.log("activateMode "+activateMode);
    $("ul.nav-tabs li").removeClass("active");
    $("div.tab-content div").removeClass("fade in active"); 
    var idName="#section"+sectionNo;   
    console.log(idName);
    var domElement = $('<li><a data-toggle="tab" id='+id+' href="'+idName+'">tab '+sectionNo+'</a></li>');
    $("#plus").before(domElement);  
    $('a[href="'+idName+'"]').parent().addClass("active");
    var domElement1 = $('<div id="section'+sectionNo+'" class="tab-pane fade"><pre id="editor'+sectionNo+'" class="editor"></h3></div>');
    $("#section0").after(domElement1);
    $(idName).addClass("in active");
    if(status==="existing")
    {
      enableEditor(filename,activateMode,sectionNo,idName); 
    }
    else
    {
      enableEditorNew(filename,activateMode,sectionNo,idName); 
    }    
    sectionNo=sectionNo+1;      
  }
  
}  
function enableEditor(filename,activateMode,sectionNo,idName)   
{  
    $('a[href="'+idName+'"]').text(filename);
    var editor="editor"+sectionNo;
    if (activateMode=="js") {activateMode="javascript"};
    console.log(filename+" to "+sectionNo+" and editor id is "+editor+" and mode "+activateMode); 
    $.ajax({
      type:'POST',
      url: '/openAjax/',
      data: {fna:text},      
      dataType:'json',
      success: function( response ) {
        // editorId=document.getElementById(editor);
        // editorId.innerText=response.content;

        // console.log(response.content);        
        editor = ace.edit(editor);
        editor.getSession().setMode("ace/mode/"+activateMode);
        editor.getSession().setValue(response.content);
         // alert("success");              
       }
      });     
    
    // $.get(text,function(data){   
    //     alert(data);     
    //     editor = ace.edit(editor);       
    //     editor.getSession().setMode("ace/mode/"+activateMode); 
    //     editor.getSession().setValue(data); 
    // }
    //     ,'text'
    //     );
}
function enableEditorNew(filename,activateMode,sectionNo,idName)   
{  
    $('a[href="'+idName+'"]').text(filename);
    var editor="editor"+sectionNo;
    if (activateMode=="js") {activateMode="javascript"};
    console.log(filename+" to "+sectionNo+" and editor id is "+editor+" and mode "+activateMode);
    editor = ace.edit(editor);     
    editor.getSession().setMode("ace/mode/"+activateMode);    
}

$("#plus").click(function(e){
  e.preventDefault();
        $('#myModal').modal('show');
});

$("#save").click(function(e){
  e.preventDefault();    
  activeTab=$("ul.nav-tabs li.active a");        
        fname=activeTab.text();
        urltoSave=activeTab.attr('id');
        fnamed=$("div.active pre div.ace_content").text();
          console.log("filename is "+fname);                              
          $.ajax({
      type:'POST',
      url: '/openTab/',
      data: {fn:fname,fd:fnamed,urltoSave:urltoSave},      
      dataType:'json',
      success: function( response ) {
         alert("success");        
         u="http://127.0.0.1:8000/static/"+fname;
         window.open(u,"runpage","heigt=300,width=200");

       }
      });
});
