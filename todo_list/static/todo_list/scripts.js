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
        document.getElementById("updateList_submit").style.display = 'block';
        document.getElementById("save_changes_info").textContent = "You have (" + numUnsavedTasks + ") unsaved changes to your To Do List. Please save now!";
    }
    else
    {
        document.getElementById("updateList_submit").style.display = 'none';
    }
}