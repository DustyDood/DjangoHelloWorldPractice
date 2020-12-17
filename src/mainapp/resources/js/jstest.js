


function beepboop() {
    //Janky! But what I'm trying to do is find the index of the selected item in the list, then load
    // the details page associated with that item in a fusion of JS and Django...
    var rexrex = document.getElementById("user_id")
    console.log(rexrex.selectedIndex)
    var user_id = parseInt(rexrex.selectedIndex) + 1
    console.log(user_id)

    //Great! user_id now gives the primary key value of the name selected in the dropdown list.
    //Now we have to load the details page using that variable!
    window.location.href = "../" + user_id + "/details/"



}
