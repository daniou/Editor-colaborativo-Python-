function send()
{    
    text = document.getElementById("text").value;
    text = text.slice(-1);
    eel.getText(text);
    setText(text);
}

function setText(text)
{
    document.getElementById("debugger").innerHTML = text
}