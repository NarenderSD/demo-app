// Copyright (c) 2024, Narender and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Scripting", {
	
    
    
    // refresh:function(frm){
    //     frappe.msgprint("🙏Ram Ram Thakur Shab");
    //     // frappe.throw("This is an error");
	// },

    // onload:function(frm){
    //     frappe.msgprint(" Hello Sonu From 'onload' event")
    // }

    // validate:function(frm){
    //     frappe.throw(" Hello Sonu From 'Validate' event")
    // }

    // before_save:function(frm){
    //     frappe.msgprint(" Hello Sonu From 'Before Save' event")
    // }

    // after_save:function(frm){
    //     frappe.msgprint(" Hello Sonu From 'After Save' event")
    // }


    // before_submit:function(frm){ 
    //     frappe.msgprint(" Hello Sonu From 'Before Submit' event")
    // }

    // enable:function(frm){
    //     frappe.msgprint(" Hello Sonu From 'Enable' event")
    // }


    // age:function(frm){
    //     if(frm.doc.age < 18){
    //         frappe.msgprint("You are not eligible to vote")
    //     }
    //     else{
    //         frappe.msgprint("You are eligible to vote")
    //     }
    // }

    // family_members_on_form_rendered:function(frm){
    //     frappe.msgprint("Hello Sonu From 'Family Members On Form Rendered' event")
    // }


    // before_submit:function(frm){
    //     frappe.msgprint("Hello Sonu From 'Before Submit' event")
    // }


    // before_insert:function(frm){
    //     frappe.msgprint("Hello Sonu From 'Before Insert' event")
    // }


    // before_save:function(frm){
    //     frappe.msgprint("Hello Sonu From 'Before Save' event")
    // }

    // before_cancel:function(frm){
    //     frappe.msgprint("Hello Sonu From 'Before Cancel' event")
    // }


// v-22


// ------------------------Value fetching-----------------------------
// frm.doc.first_name


// after_save:function(frm){
//     frappe.msgprint(__("The full name is {0}", 
//         [frm.doc.first_name + " " + frm.doc.middle_name+" "+frm.doc.last_name]))


//         for (let row of frm.doc.family_members){
//             frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'", 
//                 [row.idx,row.name1,row.relation]))
//             // [row.first_name + " " + row.middle_name+" "+row.last_name]))
//         }
// }


// ------------------------Value section end-----------------------------


// -----------------------frm,set_intro & frm.is_new-----------------------

// refresh:function(frm){
     
//     // frm.set_intro(__("This is the introduction of the form"))

//     if(frm.is_new()){
//         frm.set_intro(__("This is the introduction of the form"))
//     }
// }


// -----------------------frm.set_intro & frm.is_new section end-----------------------------


// -----------------------frm.set_value-----------------------

// validate:function(frm){
//     frm.set_value("full_name",frm.doc.first_name + " " + frm.doc.middle_name+" "+frm.doc.last_name)

//     let row = frm.add_child('family_members',{
//         name1:"Sonu",
//         relation:"Brother",
//         age:25

//     })
// }



// -----------------------frm.set_value section end-----------------------------

// -----------------------Events-----------------------


// enable:function(frm){
//    frm.set_df_property('first_name','reqd',1)
// //    frm.refresh_field('first_name');

//     frm.set_df_property('middle_name','read_only',1)
//     frm.refresh_field('middle_name');

    // frm.toggle_reqd('age',true)

    // frm.set_df_property('middle_name','reqd',1)
    // frm.set_df_property('last_name','reqd',1)
// }



// -----------------------Events section end-----------------------------


// **************************Button**************************


refresh:function(frm){

    // frm.add_custom_button('Click Me Button',() =>{
    
    // 	frappe.msgprint(__('You Clicked Me!!'));
    // })
    
    frm.add_custom_button('Click Me1',() =>{
    
        frappe.msgprint(__('You Clicked 1 !!'));
    },'click me')

    frm.add_custom_button('Click Me2',() =>{
    
        frappe.msgprint(__('You Clicked 2 !!'));
    },'click me')
}


});



// refresh:function(frm){
//     frm.add_custom_button('Click Me Button',()=>{
//         frappe.msgprint(__('You have clicked the button'));
//     })

//     frm.add_custom_button('Click Me Button 2',()=>{
//         frappe.msgprint(__('You have clicked the button 2'));
//     }, 'click me')

//     frm.add_custom_button('Click Me Button 3',()=>{
//         frappe.msgprint(__('You have clicked the button 3'));
//     },'click me')

// }

    

// });



// frappe.ui.form.on("Family Members", {
//     // cdt is the child doctype name i.e. Family Members
//     // cdn is the row name i.e. Family Members/Row1

//     // name1:function(frm) {
//     //     frappe.msgprint("Hello Sonu From 'Name' event")
//     // }

//     age:(frm, cdt, cdn) => {
//         let row = locals[cdt][cdn];
//         if(row.age < 18){
//             frappe.msgprint("You are not eligible to vote")
//         }
//         else{
//             frappe.msgprint("You are eligible to vote")
//         }
//     }

// });



