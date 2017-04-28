function countUnsavedCompletedTasks()
{
    var inputs = document.getElementsByClassName("complete_task_check");
    var numChecked = 0;
    for(var i = 0; i < inputs.length; i++) 
    {
        if(inputs[i].type == "checkbox" && inputs[i].checked == true) 
        {
            numChecked++;
        }  
    }
    
    return numChecked;
}

function addListNotifications()
{
    var numUnsavedTasks = countUnsavedCompletedTasks();
    if(numUnsavedTasks > 0)
    {
        document.getElementById("updateList_submit").setAttribute("value", "Mark " + numUnsavedTasks + " Task(s) Completed");
        document.getElementById("updateList_submit").style.display = 'block';
    }
    else
    {
        document.getElementById("updateList_submit").style.display = 'none';
    }
}