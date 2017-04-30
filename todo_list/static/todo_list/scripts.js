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
        var message = "You have unsaved changes to your To Do List ("+ numUnsavedTasks + " tasks completed). Please save your changes now!";
        if(numUnsavedTasks == 1)
        {
            message = "You have unsaved changes to your To Do List ("+ numUnsavedTasks + " task completed). Please save your changes now!";
        }
        document.getElementById("save_changes_info").textContent = message;
    }
    else
    {
        document.getElementById("updateList_submit").style.display = 'none';
    }
}

function hideOrShowCompTasks()
{
    if(document.getElementById("completed_tasks_list").classList.contains('hide_list'))
    {
        document.getElementById("show_tasks_button").textContent = "Hide Completed Tasks";
    }
    else
    {
        document.getElementById("show_tasks_button").textContent = "Show Completed Tasks";
    }
    document.getElementById("completed_tasks_list").classList.toggle('hide_list'); 
}

document.getElementById("show_tasks_button").addEventListener("click", hideOrShowCompTasks, false);