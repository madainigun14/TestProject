/*
* https://thai-notes.com/dictionaries/etymdict.html
* 
*
/
// 先勾选类型types
input_elements_types = document.querySelectorAll("div > p > label > input");

for (var i=0; i<input_elements_types.length; i++){
	let _checkbox = input_elements_types[i]
	
	if (_checkbox.checked == false){
		console.log("i: " + i.toString());
		_checkbox.click();
	} else {
		console.log("不包含checked属性");
	}
}

// 然后勾选语言langs
input_elements = document.querySelectorAll("div > label > input");

for (var i=0; i<input_elements.length; i++){
	let _checkbox = input_elements[i]

	if (_checkbox.checked == false){
		console.log("i: " + i.toString());
		_checkbox.click();
	
	} else {
		console.log("不包含checked属性");
	}
}










