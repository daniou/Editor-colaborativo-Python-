
function send()
{    
    text_area = document.getElementById("text");
    text = text_area.value;
    
    cursor = text_area.selectionStart;

    if(cursor!=0)
    {
        text = text.substring(cursor-1,cursor);
    }
    eel.getText(text);
    setText(text);
}

function setText(text)
{
    document.getElementById("debugger").innerHTML = text
}