class FontChooser extends React.Component {
    constructor(props) {
        super(props);

        var min = this.props.min > 1 ? parseInt(this.props.min) : 1;
        var max = parseInt(this.props.max);
        if (max < min)
            [min, max] = [max, min];
        var size = parseInt(this.props.size);
        if (size < min)
            size = min;
        if (size > max)
            size = max;
        var initialSize = size;

        this.state = {
            isHidden : true,
            isBold : this.props.bold == 'true',
            min : min,
            max : max,
            initialSize : initialSize,
            size : size};
    }

    toggle() {
        this.setState({isHidden : !this.state.isHidden});
    }

    changeCheckbox() {
        this.setState({isBold : !this.state.isBold});
    }

    decreaseFontSize() {
        if (this.state.size > this.state.min) {
            this.setState({size : this.state.size - 1});	
        }
    }

    increaseFontSize() {
        if (this.state.size < this.state.max) {
            this.setState({size : this.state.size + 1});	
        }
    }

    resetFontSize() {
        this.setState({size : parseInt(this.state.initialSize)});
    }

    render() {
        var weight = this.state.isBold ? 'bold' : 'normal';
        var color = (this.state.size == this.state.min || this.state.size == this.state.max) ? 'red' : 'black';
        var textStyles = {
            fontSize: this.state.size,
            fontWeight : weight
        };	

        return (
            <div>
                <input className="form" type="checkbox" id="boldCheckbox" hidden={this.state.isHidden} checked={this.state.isBold} onChange={this.changeCheckbox.bind(this)}/>
                <button className="form" id="decreaseButton" hidden={this.state.isHidden} onClick={this.decreaseFontSize.bind(this)}>-</button>
                <span className="form" id="fontSizeSpan" style={{color: color}} hidden={this.state.isHidden} onDoubleClick={this.resetFontSize.bind(this)}>{this.state.size}</span>
                <button className="form" id="increaseButton" hidden={this.state.isHidden} onClick={this.increaseFontSize.bind(this)}>+</button>
                <span id="textSpan" style={textStyles} onClick={this.toggle.bind(this)}>{this.props.text}</span>
            </div>
        );
    }
}