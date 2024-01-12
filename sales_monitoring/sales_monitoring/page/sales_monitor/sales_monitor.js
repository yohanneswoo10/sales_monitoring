frappe.pages['sales-monitor'].on_page_load = function(wrapper) {
        new MyPage(wrapper);
}

MyPage = Class.extend({
        init: function(wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Sales Monitor',
			single_column: true
		});
                // make page
                frappe.require('/assets/sales_monitoring/js/loader.js', ()=>{
                        this.make();
                })
	},
	
	// make page
        make: function(){
                // grab the class
                let me = $(this);
                // push dom elemt to page

                // execute methods
                $(frappe.render_template(`
                                <div style="text-align:center;">
				<div id="clock" style="width: 100%;font-size: 60px;font-family: Orbitron;letter-spacing: 7px;color: #17D4FE;"></div>
                                <div class="row">
                                        <div class="col"style="width: 100%;" id="desc_table"></div>
                                </div>
				<div class="row">
					<div class="col"style="width: 100%;" id="invoice"></div>
				</div>
				<div class="row">
					<div class="col"style="width: 100%;" id="so_item"></div>
				</div>
                         </div>`, this)).appendTo(this.page.main);
                sales_data();
		show_clock();
        }
	// end of class

})

let show_clock = () => {
	var date = new Date();
	var h = date.getHours(); // 0 - 23
	var m = date.getMinutes(); // 0 - 59
	var s = date.getSeconds(); // 0 - 59
	var session = "AM";
	if(h == 0){
        	h = 12;
    	}
    
    	if(h > 12){
        	h = h - 12;
        	session = "PM";
    	}
    
    	h = (h < 10) ? "0" + h : h;
    	m = (m < 10) ? "0" + m : m;
    	s = (s < 10) ? "0" + s : s;
    
    	var time = h + ":" + m + ":" + s + " " + session;
    	//document.getElementById("clock").innerText = time;
    	//document.getElementById("clock").textContent = time;
	document.querySelector('#clock').innerHTML = time;
    
    	setTimeout(show_clock, 1000);
}

let sales_data = () => {
	get_sales_order();
	get_sales_invoice();
	get_so_item();
        setTimeout(sales_data, 1000);
	//console.log("test");
	/*setTimeout(()=>{
        	get_sales_order();
                get_sales_invoice();
		//console.log("test");
        }, 100)*/
}

let get_sales_order = () => {
	frappe.call({
			async: false,
                        method: "sales_monitoring.sales_monitoring.page.sales_monitor.sales_monitor.get_sales_order", //dotted path to server method
                        callback: function(r) {
                                        // code snippet
                                        data = r.message
                                        //console.log(r);
                                        document.querySelector('#desc_table').innerHTML = data.desctable;
                        }
        })
	//setTimeout(get_sales_order, 1000);
}

let get_sales_invoice = () => {
        frappe.call({
			async: false,
                        method: "sales_monitoring.sales_monitoring.page.sales_monitor.sales_monitor.get_sales_invoice", //dotted path to server method
                        callback: function(r) {
                                        // code snippet
                                        data = r.message
                                        //console.log(r);
                                        document.querySelector('#invoice').innerHTML = data.invoices;
                        }
        })

}

let get_so_item = () => {
        frappe.call({
                        async: false,
                        method: "sales_monitoring.sales_monitoring.page.sales_monitor.sales_monitor.get_so_item", //dotted path to server method
                        callback: function(r) {
                                        // code snippet
                                        data = r.message
                                        //console.log(r);
                                        document.querySelector('#so_item').innerHTML = data.soitem;
                        }
        })

}
