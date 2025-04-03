function render({model, el}) {

    // Initialize variables
    let drawing = false;
    let gridResizing = false;
    let gridResizingMode = '';
    const container = document.createElement('div');
    const imgCanvas = document.createElement('canvas');
    const drawCanvas = document.createElement('canvas');
    const gridCanvas = document.createElement('canvas');
    const imgCtx = imgCanvas.getContext('2d');
    const drawCtx = drawCanvas.getContext('2d');
    const gridCtx = gridCanvas.getContext('2d');
    const img = new Image();

    // Set up the container
    setupContainer();

    // Load the image
    loadImage();

    // Set up event listeners
    setupEventListeners();

    // function definitions

    function setupContainer() {
        container.style.display = 'flex';
        container.style.flexDirection = 'column';
        container.style.alignItems = 'flex-start';
        container.style.justifyContent = 'center';
        el.appendChild(container);
        container.appendChild(imgCanvas);
        container.appendChild(gridCanvas);
        container.appendChild(drawCanvas);
    }

    function setCanvasSizes() {
        imgCanvas.width = img.width;
        imgCanvas.height = img.height;
        drawCanvas.width = img.width;
        drawCanvas.height = img.height;
        drawCanvas.style.marginTop = `-${img.height}px`; // Negative margin to overlay
        gridCanvas.width = img.width;
        gridCanvas.height = img.height;
        gridCanvas.style.marginTop = `-${img.height}px`; // Negative margin to overlay
    }

    function loadImage() {
        img.onload = onImageLoad;
        img.src = model.get('image_data');
    }

    function onImageLoad() {
        setCanvasSizes();
        imgCtx.drawImage(img, 0, 0);
        clearAnnotation();
        loadAnnotation();
        updateGrid();
    }

    function updateGrid() {
        clearGrid();
        if (model.get('hide_grid')) return;
        drawGrid();
    }


    function drawGrid() {
        initGridCtxOptions();

        const {padLeft, padTop, padRight, padBottom, xNum, yNum, xSize, ySize} = getGridParams();

        gridCtx.beginPath();

        for (let i = 0; i <= xNum; i += 1) {
            let x = padLeft + i * xSize;
            gridCtx.moveTo(x, padBottom);
            gridCtx.lineTo(x, gridCanvas.height - padTop);
        }
        for (let i = 0; i <= yNum; i += 1) {
            let y = padBottom + i * ySize;
            gridCtx.moveTo(padLeft, y);
            gridCtx.lineTo(gridCanvas.width - padRight, y);
        }
        gridCtx.stroke();
    }


    function getGridParams() {
        const xNum = model.get('grid_num_x');
        const yNum = model.get('grid_num_y');

        let padTop, padBottom, padLeft, padRight;

        if (model.get('change_grid')) {
            padTop = model.get('pad_top');
            padBottom = model.get('pad_bottom');
            padLeft = model.get('pad_left');
            padRight = model.get('pad_right');
        } else {
            padTop = 0;
            padBottom = 0;
            padLeft = 0;
            padRight = 0;
        }

        const gridWidth = gridCanvas.width - padLeft - padRight;
        const gridHeight = gridCanvas.height - padTop - padBottom;

        const xSize = gridWidth / xNum;
        const ySize = gridHeight / yNum;

        return {padLeft, padTop, padRight, padBottom, xNum, yNum, xSize, ySize};
    }

    function loadAnnotation() {
        if (model.get('change_grid')) return;
        const annotated_image = model.get('annotated_image');
        if (annotated_image) {
            loadAndDrawImage(annotated_image, drawCtx);
        }
    }

    function setupEventListeners() {
        drawCanvas.addEventListener('mousedown', onMouseDown);
        drawCanvas.addEventListener('mousemove', onMouseMove);
        // drawCanvas.addEventListener('mouseup', onMouseUp);
        document.addEventListener('mouseup', (e) => {
            onMouseUp();
        });

        model.on("change:mode", changeCursorStyleForDrawing);
        model.on("change:brush_size", changeCursorStyleForDrawing);
        model.on("change:annotated_image", onAnnotationChanged);
        model.on("change:change_grid", onChangeGridModeChanged);
        model.on("change:image_data", onImageDataChanged);
        model.on("change:grid_num_x", updateGrid);
        model.on("change:grid_num_y", updateGrid);
        model.on("change:hide_grid", updateGrid);
    }


    function onMouseDown(e) {
        startDrawingIfEnabled(e);
        startResizingIfEnabled(e);
    }

    function onMouseMove(e) {
        drawingOnMouseMoveIfEnabled(e);
        resizeGridIfEnabled(e);
        changeCursorStyleForResizing(e);
    }

    function onMouseUp() {
        finishDrawingIfEnabled();
        finishResizingIfEnabled();
    }

    function startDrawingIfEnabled(e) {
        if (model.get('mode') === 'Off') return;
        drawing = true;
        setCtxOptions();
        if (model.get('mode') === 'Erase') {
            drawCtx.globalCompositeOperation = 'destination-out';
        }
        drawCtx.beginPath();
        drawCtx.moveTo(e.offsetX, e.offsetY);
        drawCtx.lineTo(e.offsetX, e.offsetY); // Draw a tiny line to the same point
        drawCtx.stroke(); // Stroke the line to make the dot visible
        drawCtx.moveTo(e.offsetX, e.offsetY);
    }

    function startResizingIfEnabled(e) {
        if (!model.get('change_grid')) return;
        if (gridResizingMode === '') return;
        gridResizing = true;
    }

    function drawingOnMouseMoveIfEnabled(e) {
        if (drawing && e.buttons === 1) {
            drawCtx.lineTo(e.offsetX, e.offsetY);
            drawCtx.stroke();
        } else if (drawing) {
            finishDrawingIfEnabled();
        }
    }

    function resizeGridIfEnabled(e) {
        if (gridResizing && e.buttons === 1) {

            const x = Math.round(e.offsetX);
            const y = Math.round(e.offsetY);
            const w = Math.round(gridCanvas.width);
            const h = Math.round(gridCanvas.height);

            switch (gridResizingMode) {
                case 'left':
                    model.set('pad_left', x);
                    break;
                case 'right':
                    model.set('pad_right', w - x);
                    break;
                case 'top':
                    model.set('pad_top', h - y);
                    break;
                case 'bottom':
                    model.set('pad_bottom', y);
                    break;
                case 'left-top':
                    model.set('pad_left', x);
                    model.set('pad_top', h - y);
                    break;
                case 'left-bottom':
                    model.set('pad_left', x);
                    model.set('pad_bottom', y);
                    break;
                case 'right-top':
                    model.set('pad_right', w - x);
                    model.set('pad_top', h - y);
                    break;
                case 'right-bottom':
                    model.set('pad_right', w - x);
                    model.set('pad_bottom', y);
                    break;
            }

            model.save_changes();

            updateGrid();

        } else if (gridResizing) {
            gridResizing = false;
        }
    }

    function finishDrawingIfEnabled() {
        if (!drawing) return;
        setNonZeroPixelsToColor();
        saveAnnotation();
        resetCtxOptions();
        drawing = false;
    }

    function finishResizingIfEnabled() {
        if (!gridResizing) return;
        gridResizing = false;
        drawCanvas.style.cursor = 'default';
        gridResizingMode = '';
    }

    function onChangeGridModeChanged() {
        drawCanvas.style.cursor = 'default';  // Reset cursor in any case
    }

    function onAnnotationChanged() {
        if (drawing) return;
        clearAnnotation();
        loadAnnotation();
    }

    function onImageDataChanged() {
        clearImage();
        clearAnnotation();
        loadImage();
    }

    function saveAnnotation() {
        if (model.get('change_grid')) return;
        model.set('annotated_image', drawCanvas.toDataURL());
        model.save_changes();
    }

    function clearAnnotation() {
        clearCanvas(drawCanvas, drawCtx);
    }

    function clearImage() {
        clearCanvas(imgCanvas, imgCtx);
    }

    function clearGrid() {
        clearCanvas(gridCanvas, gridCtx);
    }

    function clearCanvas(canvas, ctx) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function setCtxOptions() {
        drawCtx.lineWidth = model.get('brush_size');
        drawCtx.lineCap = 'round';
        drawCtx.strokeStyle = "#FF0000";
        drawCtx.fillStyle = "#FF0000";
    }

    function initGridCtxOptions() {
        gridCtx.lineWidth = 1;
        gridCtx.lineCap = 'round';
        gridCtx.strokeStyle = "#000000";
        gridCtx.fillStyle = "#000000";
    }

    function resetCtxOptions() {
        drawCtx.lineWidth = 1;
        drawCtx.lineCap = 'butt';
        drawCtx.strokeStyle = "#000000";
        drawCtx.fillStyle = "#000000";
        drawCtx.globalAlpha = 1.0;
        drawCtx.globalCompositeOperation = 'source-over';
    }

    function loadAndDrawImage(url, ctx) {
        const img = new Image();
        img.onload = function () {
            ctx.drawImage(img, 0, 0);
        };
        img.src = url;
    }

    function setNonZeroPixelsToColor() {
        let imageData = drawCtx.getImageData(0, 0, imgCanvas.width, imgCanvas.height);
        let data = imageData.data;

        for (let i = 0; i < data.length; i += 4) {
            if (data[i + 3] !== 0) { // If the pixel is not fully transparent
                data[i] = 255; // Set to red
                data[i + 1] = 0; // Set to green
                data[i + 2] = 0; // Set to blue
                data[i + 3] = 128; // Set opacity to 0.5
            }
        }

        drawCtx.putImageData(imageData, 0, 0);
    }


    function isMouseNearGridEdge(mouseX, mouseY) {
        const edgeThreshold = 10; // Pixels near edge to consider for resizing
        const {padLeft, padTop, padRight, padBottom, xNum, yNum, xSize, ySize} = getGridParams();

        const withinX = (mouseX > padLeft - edgeThreshold) && (mouseX < gridCanvas.width - padRight + edgeThreshold);
        if (!withinX) return {nearLeftEdge: false, nearRightEdge: false, nearTopEdge: false, nearBottomEdge: false};
        const withinY = (mouseY > padBottom - edgeThreshold) && (mouseY < gridCanvas.height - padTop + edgeThreshold);
        if (!withinY) return {nearLeftEdge: false, nearRightEdge: false, nearTopEdge: false, nearBottomEdge: false};

        const nearLeftEdge = (Math.abs(mouseX - padLeft) < edgeThreshold);
        const nearRightEdge = (Math.abs(mouseX - (gridCanvas.width - padRight)) < edgeThreshold);
        const nearBottomEdge = (Math.abs(mouseY - padBottom) < edgeThreshold);
        const nearTopEdge = (Math.abs(mouseY - (gridCanvas.height - padTop)) < edgeThreshold);

        return {nearLeftEdge, nearRightEdge, nearTopEdge, nearBottomEdge};
    }


    function changeCursorStyleForDrawing(e) {
        if (model.get('mode') === 'Off') {
            drawCanvas.style.cursor = 'default';
            return;
        }
        if (model.get('mode') === 'Erase') {
            drawCanvas.style.cursor = generateCircleCursorDataURL(model.get('brush_size'), 'white');
        } else {
            drawCanvas.style.cursor = generateCircleCursorDataURL(model.get('brush_size'), 'red');
        }

    }

    function changeCursorStyleForResizing(e) {
        if (model.get('hide_grid')) return;
        if (model.get('change_grid') === false) return;
        // if button is pressed, don't change cursor
        if (e.buttons === 1) return;

        const {nearLeftEdge, nearRightEdge, nearTopEdge, nearBottomEdge} = isMouseNearGridEdge(e.offsetX, e.offsetY);

        if (nearLeftEdge && nearTopEdge) {
            drawCanvas.style.cursor = 'sw-resize';
            gridResizingMode = 'left-top';
        } else if (nearLeftEdge && nearBottomEdge) {
            drawCanvas.style.cursor = 'nw-resize';
            gridResizingMode = 'left-bottom';
        } else if (nearRightEdge && nearTopEdge) {
            drawCanvas.style.cursor = 'se-resize';
            gridResizingMode = 'right-top';
        } else if (nearRightEdge && nearBottomEdge) {
            drawCanvas.style.cursor = 'ne-resize';
            gridResizingMode = 'right-bottom';
        } else if (nearLeftEdge) {
            drawCanvas.style.cursor = 'ew-resize';
            gridResizingMode = 'left';
        } else if (nearRightEdge) {
            drawCanvas.style.cursor = 'ew-resize';
            gridResizingMode = 'right';
        } else if (nearTopEdge) {
            drawCanvas.style.cursor = 'ns-resize';
            gridResizingMode = 'top';
        } else if (nearBottomEdge) {
            drawCanvas.style.cursor = 'ns-resize';
            gridResizingMode = 'bottom';
        } else {
            drawCanvas.style.cursor = 'default';
            gridResizingMode = '';
        }
    }


    function generateCircleCursorDataURL(circleSize, color) {
        // Define the SVG content
        const svg = `
<svg xmlns="http://www.w3.org/2000/svg" width="${circleSize}" height="${circleSize}">
    <circle cx="${circleSize / 2}" cy="${circleSize / 2}" r="${circleSize / 2}" fill="${color}" />
</svg>`;

        // Encode the SVG to be used in a URL
        const encodedSVG = encodeURIComponent(svg);

        // Create the data URL, incorporating the encoded SVG
        const dataURL = `data:image/svg+xml;utf8,${encodedSVG}`;

        // The hotspot coordinates should be the center of the circle
        const hotspotX = circleSize / 2;
        const hotspotY = circleSize / 2;

        return `url('${dataURL}') ${hotspotX} ${hotspotY}, auto`;
    }
}

export default {render};
