import './about.css';
import aboutImage from '../../assets/about_image.png'; // Import your image file

const AboutPage = () => {
    return (
        <div className="about-container">
            <div className="about-page1">
                <div className="text-section">
                    <h1>Empo Vr</h1>
                    <h2>Empo Vr</h2>
                    <p>EmpoVR is a Mythyaverse solution that uses Virtual Reality and AI to promote holistic wellness among employees. It offers guided meditation, personalized workouts, cognitive games, social connectivity, and AI-driven financial decision-making, enhancing mental and physical health.</p>
                    <button className='load'>Load More</button>
                </div>
                <div className="image-section">
                    <div className="rect1"></div>
                    <div className="rect2"></div>
                    <div className="rect3">
                        <button className="button">VR Placed</button>
                        <button className="button">Education</button>
                        <button className="button">Placement</button>
                    </div>
                </div>
            </div>

            <div className='testimonials-section'>
                <h2>Testimonials</h2>
                <div className="testimonial">
                    <h3>Check What our Students are saying about VR Placed</h3>
                    <div className="testimonial-content">
                        <div className='testimonial-image'></div> {/* Replaced image tag with a div */}
                        <div className="testimonial-text">
                            <p>"VR Placed is Reliable, Fast, and Helpful"</p>
                            <h4>We Didn't say it. Our customer did.</h4>
                            <div className="circles-container">
                                <div className="circle1"></div>
                                <div className="circle"></div>
                                <div className="circle"></div>
                                <div className="circle"></div>
                            </div>
                            <p className='testimonial-author'>AR Shakir</p>
                            <p className='testimonial-sub'>Student of Astreya</p>
                        </div>
                    </div>
                </div>
            </div>

            <div className="about-page1 reverse-layout">
            <div className="text-section">
                    <h1>Blockchain as service</h1>
                    <h2>Blockchain service</h2>
                    <p>Our Blockchain as a Service (BaaS) platform simplifies workflows and improves data security, integrating with existing systems. Built on Enterprise Hyperledger Fabric, it offers transparency, regulatory compliance, and global support. </p>
                    <button className='load'>Load More</button>
                </div>
                <div className="image-section">
                    <div className="rect3"></div>
                    <div className="rect2"></div>
                    <div className="rect1">
                        <button className="button">VR Placed</button>
                        <button className="button">Education</button>
                        <button className="button">Placement</button>
                    </div>
                </div>
                
            </div>

            <div className='testimonials-section'>
                <h2>Testimonials</h2>
                <div className="testimonial">
                    <h3>Check What our Students are saying about VR Placed</h3>
                    <div className="testimonial-content">
                        <div className='testimonial-image'></div> {/* Replaced image tag with a div */}
                        <div className="testimonial-text">
                            <p>"VR Placed is Reliable, Fast, and Helpful"</p>
                            <h4>We Didn't say it. Our customer did.</h4>
                            <div className="circles-container">
                                <div className="circle1"></div>
                                <div className="circle"></div>
                                <div className="circle"></div>
                                <div className="circle"></div>
                            </div>
                            <p className='testimonial-author'>AR Shakir</p>
                            <p className='testimonial-sub'>Student of Astreya</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AboutPage;
