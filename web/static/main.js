
document.addEventListener("keypress", KeyCheck); //al presionar una tecla llama keycheck
function KeyCheck(event)
{
    var KeyID = event.keyCode;
    //Comprueba que el texteare este seleccionado
    if (document.activeElement.id != "text") return;

    text_area = document.getElementById("text");
    text = text_area.value;
    pointer = text_area.selectionStart;

    switch(KeyID)
    {
        case 8:
            del(pointer)
        break; 
        case 46:
            supr(pointer)
        break;
        default:
            write(pointer,String.fromCharCode(KeyID))
        break;
    }
    
}

function del(pointer)
{    
    eel.edit("delete",pointer);
}

function supr(pointer)
{    
    eel.edit("supr",pointer);
}


function write(pointer,text)
{    
    eel.edit("insert",pointer,text);
    setText(text);
}

function setText(text)
{
    document.getElementById("debugger").innerHTML = text
}