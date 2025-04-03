function getXPath(element) {
    if (element.id) {
        return "//*[@id='" + element.id + "']";
    }
    
    if (element == document.body) {
        return '/html/body';
    }
    
    let path = '';
    while (element && element.nodeType === 1) {
        let index = 1;
        let sibling = element.previousSibling;
        while (sibling) {
            if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
                index++;
            }
            sibling = sibling.previousSibling;
        }
        const tagName = element.tagName.toLowerCase();
        path = '/' + tagName + '[' + index + ']' + path;
        element = element.parentNode;
    }
    return path;
}

function getCssPath(element) {
    if (element.id) {
        return '#' + element.id;
    }
    
    let path = '';
    while (element && element.nodeType === 1) {
        let selector = element.tagName.toLowerCase();
        if (element.id) {
            selector += '#' + element.id;
        } else if (element.className) {
            selector += '.' + element.className.split(' ').join('.');
        }
        path = selector + (path ? ' > ' + path : '');
        element = element.parentNode;
    }
    return path;
} 