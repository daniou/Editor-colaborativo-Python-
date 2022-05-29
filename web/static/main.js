
function send()
{    
    text_area = document.getElementById("text");
    text = text_area.value;
    
    pointer = text_area.selectionStart;

    if(pointer!=0)
    {
        text = text.substring(pointer-1,pointer);
    }
    eel.getText(pointer,text);
    setText(text);
}

function setText(text)
{
    document.getElementById("debugger").innerHTML = text
}